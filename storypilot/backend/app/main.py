import os
def _load_env():
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            l = l.strip()
            if l and not l.startswith("#") and "=" in l: k, v = l.split("=", 1); os.environ.setdefault(k.strip(), v.strip().strip('"'))
_load_env()
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .store import Store
from . import workflow as w, connectors as cn
from .data import DOCS
app = FastAPI(title="StoryPilot"); st = Store()
class Review(BaseModel): decision: str; response: str | None = None
class ImportReq(BaseModel): key: str; confluence: bool = True
def rec_or_404(sid):
    r = st.get(sid)
    if not r: raise HTTPException(404, "Story not found")
    return r
@app.get("/api/mode")
def mode():
    live = bool(os.environ.get("GOOGLE_CLOUD_PROJECT")) and os.environ.get("USE_GEMINI", "1") == "1"
    return {"store": st.mode, "ai": "gemini-live" if live else "cached-offline", "model": os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"),
            "jira": cn.configured(), "source": "demo fixtures plus live Jira/Confluence imports"}
@app.get("/api/stories")
def stories(): return sorted(st.list(), key=lambda r: r["story_id"])
@app.get("/api/stories/{sid}")
def story(sid: str):
    r = rec_or_404(sid); docs = {**DOCS, **r.get("source_docs", {})}
    return {**r, "source_docs": {s: docs[s] for s in r["source_ids"] if s in docs}}
@app.post("/api/import/jira")
def import_jira(b: ImportReq):
    try: s = cn.import_story(b.key, b.confluence)
    except cn.ConnectorError as e: raise HTTPException(502, str(e))
    rec = st.new(s); w.audit(rec, "imported_from_jira", sources=len(s["source_ids"])); st.put(rec); return rec
@app.post("/api/stories/{sid}/analyze")
def analyze(sid: str):
    try: r = w.analyze(rec_or_404(sid))
    except RuntimeError as e: raise HTTPException(502, str(e))
    st.put(r); return r
@app.post("/api/stories/{sid}/review/{kind}/{iid}")
def review(sid: str, kind: str, iid: str, body: Review):
    try: r = w.review(rec_or_404(sid), kind, iid, body.decision, body.response)
    except (KeyError, ValueError) as e: raise HTTPException(400, f"Invalid action: {e}")
    st.put(r); return r
@app.post("/api/stories/{sid}/docs")
def docs(sid: str):
    r = rec_or_404(sid)
    if not r["trace"]: raise HTTPException(400, "Analyze the story first.")
    r = w.draft_docs(r); st.put(r); return r
@app.get("/api/stories/{sid}/docs.md", response_class=PlainTextResponse)
def docs_md(sid: str):
    d = rec_or_404(sid).get("docs")
    if not d: raise HTTPException(404, "No draft yet")
    return d["markdown"]
@app.get("/api/queue")
def queue():
    q = []
    for r in st.list():
        q += [{"story_id": r["story_id"], "kind": "questions", "id": x["question_id"], "text": x["text"], "status": x["status"]} for x in r["questions"] if x["status"] == "awaiting_review"]
        if r.get("docs") and r["docs"]["status"] == "awaiting_review": q.append({"story_id": r["story_id"], "kind": "docs", "id": "docs", "text": "Completion documentation draft", "status": "awaiting_review"})
    return q
@app.get("/api/eval")
def ev(): return w.evaluate(st.list())
if os.path.isdir("static"):
    app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")
    @app.get("/{p:path}")
    def spa(p: str): return FileResponse("static/index.html")
