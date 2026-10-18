"""Labelled SYNTHETIC demo data. Source mode: demo fixtures (no real Jira/GitHub)."""
DOCS = {
 "SRC-1": {"name": "Payment API Guidelines", "version": "v2", "date": "2026-01-10", "origin": "demo fixture",
  "text": "Requests must include a valid access token. Invalid requests return HTTP 400 with an error body containing code and message. Amount must be a positive decimal."},
 "SRC-2": {"name": "Error Handling Standard", "version": "v1", "date": "2025-03-02", "origin": "demo fixture",
  "text": "Invalid requests return HTTP 422 with a field-level errors array. All errors are logged with a correlation id."},
 "SRC-D1": {"name": "Diff: validators.py", "version": "pr-41", "date": "2026-02-01", "origin": "supplied diff (demo)",
  "text": "+ if not req.account_id: raise ApiError(400, 'ACCOUNT_REQUIRED') + if req.amount <= 0: raise ApiError(400, 'AMOUNT_INVALID')"},
 "SRC-T1": {"name": "Test run: test_validators", "version": "ci-88", "date": "2026-02-01", "origin": "supplied test evidence (demo)",
  "text": "PASS test_missing_account_rejected PASS test_negative_amount_rejected"},
}
def F(key, cat, sev, stmt, ev, why, q, conf="medium"):
    return {"key": key, "category": cat, "severity": sev, "statement": stmt, "evidence": [{"source_id": s, "excerpt": e} for s, e in ev],
            "reasoning_summary": why, "suggested_question": q, "confidence": conf, "review_status": "pending"}
GOLD = {"STORY-100": [], "STORY-101": ["expired_token", "amount_limit"], "STORY-102": ["status_conflict"]}
# Cached analysis: used offline or when Gemini is unavailable. Excerpts must be exact substrings of the sources.
CACHED = {
 "STORY-100": {"findings": [], "trace": [
   {"ac_id": "AC-1", "status": "supported", "evidence": [{"source_id": "SRC-D1", "excerpt": "raise ApiError(400, 'ACCOUNT_REQUIRED')"}, {"source_id": "SRC-T1", "excerpt": "PASS test_missing_account_rejected"}]},
   {"ac_id": "AC-2", "status": "supported", "evidence": [{"source_id": "SRC-D1", "excerpt": "raise ApiError(400, 'AMOUNT_INVALID')"}, {"source_id": "SRC-T1", "excerpt": "PASS test_negative_amount_rejected"}]}]},
 "STORY-101": {"findings": [
   F("expired_token", "missing_requirement", "high", "Response for an expired access token is not specified.", [("SRC-1", "Requests must include a valid access token.")],
     "Source requires a valid token but defines no response for an expired one.", "What response should the API return when the access token has expired?"),
   F("amount_limit", "missing_requirement", "medium", "Maximum payment amount is not defined.", [("SRC-1", "Amount must be a positive decimal.")],
     "Only a lower bound is stated; no upper limit or precision rule.", "Is there a maximum amount or decimal precision to enforce?", "low")],
  "trace": [{"ac_id": "AC-1", "status": "supported", "evidence": [{"source_id": "SRC-D1", "excerpt": "raise ApiError(400, 'ACCOUNT_REQUIRED')"}]},
            {"ac_id": "AC-2", "status": "no_evidence", "evidence": []}, {"ac_id": "AC-3", "status": "unknown", "evidence": []}]},
 "STORY-102": {"findings": [
   F("status_conflict", "contradiction", "high", "Two sources specify different status codes for invalid requests.",
     [("SRC-1", "Invalid requests return HTTP 400"), ("SRC-2", "Invalid requests return HTTP 422")],
     "SRC-1 (v2, 2026-01) says 400; SRC-2 (v1, 2025-03) says 422. Newer is not automatically authoritative.", "Which status code is canonical for invalid payment requests: 400 or 422?", "high")],
  "trace": [{"ac_id": "AC-1", "status": "conflicting", "evidence": [{"source_id": "SRC-D1", "excerpt": "raise ApiError(400, 'AMOUNT_INVALID')"}, {"source_id": "SRC-2", "excerpt": "Invalid requests return HTTP 422"}]}]},
}
STORIES = [
 {"story_id": "STORY-100", "title": "Reject missing account and non-positive amounts", "description": "Validate payment requests before processing.", "priority": "high",
  "acceptance_criteria": [{"id": "AC-1", "text": "Missing account identifiers are rejected"}, {"id": "AC-2", "text": "Non-positive amounts are rejected"}], "source_ids": ["SRC-1", "SRC-D1", "SRC-T1"]},
 {"story_id": "STORY-101", "title": "Harden payment authentication and limits", "description": "Enforce token validity and amount rules on payment requests.", "priority": "high",
  "acceptance_criteria": [{"id": "AC-1", "text": "Missing account identifiers are rejected"}, {"id": "AC-2", "text": "Expired tokens are handled"}, {"id": "AC-3", "text": "Oversized amounts are rejected"}], "source_ids": ["SRC-1", "SRC-D1"]},
 {"story_id": "STORY-102", "title": "Standardise invalid-request error response", "description": "Invalid requests must return the documented error response.", "priority": "medium",
  "acceptance_criteria": [{"id": "AC-1", "text": "Invalid requests return the documented error response"}], "source_ids": ["SRC-1", "SRC-2", "SRC-D1"]},
]
