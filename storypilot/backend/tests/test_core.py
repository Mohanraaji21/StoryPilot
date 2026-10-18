import os, sys, tempfile; sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
os.environ["STORE_PATH"] = os.path.join(tempfile.mkdtemp(), "s.json"); os.environ.pop("GOOGLE_CLOUD_PROJECT", None)
from app import connectors as c, workflow as w
from app.store import Store
import io, urllib.error

def test_adf_and_ac():
    adf = {"type": "doc", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Acceptance Criteria"}]}, {"type": "paragraph", "content": [{"type": "text", "text": "Expired tokens return 401"}]}]}
    ac = c.parse_ac(c.adf_text(adf)); assert ac == [{"id": "AC-1", "text": "Expired tokens return 401"}]
def test_key_validation():
    try: c.import_story("bad key"); assert False
    except c.ConnectorError: pass
def test_unconfigured():
    for k in ("ATLASSIAN_BASE_URL", "ATLASSIAN_EMAIL", "ATLASSIAN_API_TOKEN"): os.environ.pop(k, None)
    assert not c.configured()
def test_http_error_includes_atlassian_message():
    original_cfg, original_open = c.cfg, c.urllib.request.urlopen
    c.cfg = lambda: {"base": "https://example.atlassian.net", "email": "user@example.com", "token": "test-token"}
    def fail_request(req, timeout=20):
        raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, io.BytesIO(
            b'{"errorMessages":["Issue does not exist or you do not have permission to see it."],"errors":{}}'))
    c.urllib.request.urlopen = fail_request
    try:
        try:
            c._get("/rest/api/3/issue/SCRUM-1")
            assert False
        except c.ConnectorError as e:
            assert "HTTP 404" in str(e)
            assert "browse its project and issue" in str(e)
            assert "Issue does not exist or you do not have permission to see it." in str(e)
    finally:
        c.cfg, c.urllib.request.urlopen = original_cfg, original_open
def test_invalid_evidence_dropped():
    assert not w.valid_ref({"source_id": "S", "excerpt": "nope"}, ["S"], {"S": {"text": "abc"}}); assert w.valid_ref({"source_id": "S", "excerpt": "ab"}, ["S"], {"S": {"text": "abc"}})
def test_demo_flow_and_eval():
    s = Store()
    for r in s.list(): w.analyze(r); w.draft_docs(r); s.put(r)
    e = w.evaluate(s.list()); assert e["recall"] == 1.0 and e["precision"] == 1.0 and e["evidence_validity"] == 1.0
def test_imported_story_needs_live_ai():
    r = Store().new({"story_id": "X-1", "title": "t", "description": "", "priority": "low", "acceptance_criteria": [], "source_ids": []})
    try: w.analyze(r); assert False
    except RuntimeError: pass
if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"): f(); print("ok", n)
