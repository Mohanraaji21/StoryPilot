import json, os, threading, copy
from .data import STORIES
class Store:
    """Firestore when GOOGLE_CLOUD_PROJECT is set and reachable; otherwise a local JSON file."""
    def __init__(self):
        self.path = os.environ.get("STORE_PATH", "store.json"); self.lock = threading.Lock(); self.fs = None; self.mode = "local-json"
        if os.environ.get("GOOGLE_CLOUD_PROJECT"):
            try:
                from google.cloud import firestore
                self.fs = firestore.Client(); self.mode = "firestore"
            except Exception as e: print("Firestore unavailable, using JSON:", e)
        if not self.list():
            for s in STORIES: self.put(self.new(s))
    def new(self, s):
        return {**copy.deepcopy(s), "status": "assigned", "findings": [], "questions": [], "decisions": [], "trace": [], "docs": None,
                "audit_events": [], "analysis_stats": None}
    def _all(self):
        if not os.path.exists(self.path): return {}
        return json.load(open(self.path))
    def list(self):
        if self.fs: return [d.to_dict() for d in self.fs.collection("stories").stream()]
        return list(self._all().values())
    def get(self, sid):
        if self.fs:
            d = self.fs.collection("stories").document(sid).get(); return d.to_dict() if d.exists else None
        return self._all().get(sid)
    def put(self, rec):  # last valid record is preserved if serialisation fails
        if self.fs: return self.fs.collection("stories").document(rec["story_id"]).set(rec)
        with self.lock:
            a = self._all(); a[rec["story_id"]] = rec; tmp = self.path + ".tmp"
            json.dump(a, open(tmp, "w"), indent=1); os.replace(tmp, self.path)
