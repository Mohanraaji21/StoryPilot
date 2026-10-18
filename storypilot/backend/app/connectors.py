"""Read-only Jira Cloud and Confluence Cloud connectors (stdlib only). Credentials come from environment variables."""
import base64, json, os, re, urllib.error, urllib.parse, urllib.request
from html import unescape
class ConnectorError(Exception): pass
def cfg():
    legacy_base = os.environ.get("ATLASSIAN_BASE_URL", "").strip()
    return {
        "jira_base": os.environ.get("ATLASSIAN_JIRA_BASE_URL", "").strip() or legacy_base,
        "confluence_base": os.environ.get("ATLASSIAN_CONFLUENCE_BASE_URL", "").strip() or legacy_base,
        "email": os.environ.get("ATLASSIAN_EMAIL", "").strip(),
        "token": os.environ.get("ATLASSIAN_API_TOKEN", "").strip(),
    }
def configured():
    c = cfg()
    return all((c["jira_base"], c["email"], c["token"]))
def _get(path, params=None, product="jira"):
    c = cfg()
    base = c.get(f"{product}_base", "")
    if not all((base, c["email"], c["token"])):
        raise ConnectorError("Atlassian is not configured. Set ATLASSIAN_JIRA_BASE_URL, ATLASSIAN_EMAIL and ATLASSIAN_API_TOKEN; set ATLASSIAN_CONFLUENCE_BASE_URL to enable Confluence search.")
    url = base.rstrip("/") + path + ("?" + urllib.parse.urlencode(params) if params else "")
    auth = base64.b64encode(f"{c['email']}:{c['token']}".encode()).decode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": "Basic " + auth, "Accept": "application/json"}), timeout=20) as r: return json.load(r)
    except urllib.error.HTTPError as e:
        hint = {
            401: "check the Atlassian email and API token",
            403: "this account lacks permission",
            404: "confirm the requested resource exists on this site and this account can access it",
        }.get(e.code, "")
        provider_message = ""
        try:
            payload = json.loads(e.read().decode("utf-8"))
            if isinstance(payload, dict):
                messages = payload.get("errorMessages", [])
                if isinstance(messages, list):
                    provider_message = "; ".join(m for m in messages if isinstance(m, str))
                errors = payload.get("errors", {})
                if isinstance(errors, dict):
                    field_messages = [m for m in errors.values() if isinstance(m, str)]
                    if field_messages:
                        provider_message = "; ".join(filter(None, [provider_message, *field_messages]))
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass
        detail = f"Atlassian returned HTTP {e.code} for {path}"
        if hint: detail += f" ({hint})"
        if provider_message: detail += f". Atlassian: {provider_message[:300]}"
        raise ConnectorError(detail) from e
    except Exception as e: raise ConnectorError(f"Could not reach Atlassian: {e}") from e
def adf_text(n):
    if isinstance(n, str): return n
    if not isinstance(n, dict): return ""
    t = n.get("type")
    if t == "text": return n.get("text", "")
    if t == "hardBreak": return "\n"
    return "".join(adf_text(c) for c in n.get("content") or []) + ("\n" if t in ("paragraph", "heading", "tableRow") else "")
def html_text(h): return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", h or ""))).strip()
def parse_ac(text):
    lines = [l.strip(" -*\u2022\t") for l in text.splitlines() if l.strip()]; out = []; on = False
    for l in lines:
        if re.match(r"(?i)acceptance criteria", l): on = True; continue
        if on and re.match(r"(?i)(description|notes|out of scope|technical details)\b.*:?$", l) and len(l) < 30: break
        if on: out.append(l)
    if not out: out = [l for l in lines if re.match(r"(?i)(given |when |then |ac\s*\d*\s*[:.)])", l)]
    return [{"id": f"AC-{i+1}", "text": l} for i, l in enumerate(out[:15])]
def chunk(t, n=900):
    out, cur = [], ""
    for w in t.split():
        if len(cur) + len(w) + 1 > n: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + ([cur] if cur else [])
def top_chunks(docs, query, k=8):
    q = {w.lower() for w in re.findall(r"[A-Za-z0-9]{4,}", query)}
    score = lambda d: sum(1 for w in q if w in d["text"].lower())
    return dict(sorted(docs.items(), key=lambda kv: -score(kv[1]))[:k])
def confluence_chunks(text, key, pages=5):
    uniq = list(dict.fromkeys(w.lower() for w in re.findall(r"[A-Za-z0-9]{4,}", text)))[:6]
    terms = " OR ".join(f'text ~ "{w}"' for w in uniq + [key])
    data = _get("/wiki/rest/api/content/search", {"cql": f"type=page AND ({terms})", "limit": pages, "expand": "body.storage,version"}, product="confluence")
    out = {}
    for p in data.get("results", []):
        plain = html_text(p["body"]["storage"]["value"]); v = p.get("version", {})
        for n, ch in enumerate(chunk(plain)):
            out[f"CONF-{p['id']}-{n+1}"] = {"name": f"{p['title']} (part {n+1})", "version": f"v{v.get('number', '?')}", "date": (v.get("when") or "")[:10], "origin": "Confluence (live)", "text": ch}
    return top_chunks(out, text)
def import_story(key, with_confluence=True):
    key = key.strip().upper()
    if not re.fullmatch(r"[A-Z][A-Z0-9_]+-\d+", key): raise ConnectorError("Invalid Jira key. Expected a format like PAY-123.")
    f = _get(f"/rest/api/3/issue/{key}", {"fields": "summary,description,priority,status,updated"})["fields"]
    desc = adf_text(f.get("description")).strip(); ac = parse_ac(desc); warns = []
    if not desc: warns.append("The Jira description is empty.")
    if not ac: warns.append("No acceptance criteria found. Add an 'Acceptance Criteria' section to the Jira description.")
    docs = {f"JIRA-{key}": {"name": f"Jira {key}: {f['summary']}", "version": (f.get("status") or {}).get("name", ""), "date": (f.get("updated") or "")[:10], "origin": "Jira (live)", "text": f"{f['summary']}\n{desc}"}}
    if with_confluence:
        try: docs.update(confluence_chunks(f"{f['summary']} {desc}", key))
        except ConnectorError as e: warns.append(f"Confluence search skipped: {e}")
    return {"story_id": key, "title": f["summary"], "description": desc[:600], "priority": ((f.get("priority") or {}).get("name") or "unknown").lower(),
            "acceptance_criteria": ac, "source_ids": list(docs), "source_docs": docs, "import_warnings": warns}
