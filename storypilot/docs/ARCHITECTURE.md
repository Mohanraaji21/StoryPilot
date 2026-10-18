# StoryPilot architecture and coverage

## Flow
Sources (Jira story, Confluence pages, or demo fixtures) > ingest into one story record > retrieve relevant evidence > Gemini structured analysis > deterministic evidence validation > human approval queue > documentation draft > audit trail and evaluation.

## Components
| Part | File | Role |
|---|---|---|
| API | `backend/app/main.py` | FastAPI routes, `.env` loader, serves the built UI |
| Connectors | `backend/app/connectors.py` | Read-only Jira and Confluence over REST; ADF and HTML to text; acceptance-criteria parsing; chunking; keyword ranking |
| Workflow | `backend/app/workflow.py` | Gemini call, evidence validation, review, docs draft, evaluation |
| Store | `backend/app/store.py` | Firestore, or a local JSON file when Firestore is unavailable |
| Demo data | `backend/app/data.py` | Three synthetic stories, sources, cached outputs and gold gaps |
| UI | `frontend/src/App.jsx` | Today and import, Story, Approval queue, Evaluation |
| Tests | `backend/tests/test_core.py` | Parsing, validation, offline flow, evaluation |

## API
`GET /api/mode`, `GET /api/stories`, `GET /api/stories/{id}`, `POST /api/import/jira {key, confluence}`, `POST /api/stories/{id}/analyze`, `POST /api/stories/{id}/review/{questions|docs}/{id}`, `POST /api/stories/{id}/docs`, `GET /api/stories/{id}/docs.md`, `GET /api/queue`, `GET /api/eval`.

## Trust rules
- Source text is untrusted data. The prompt tells Gemini to ignore instructions inside it.
- A finding with no valid evidence reference is dropped. An excerpt must be an exact substring of a loaded source.
- "No evidence" means none was supplied, never "not implemented".
- Every output waits for human approval. Approving a question is a simulated send, so nothing is posted to Jira or Confluence (the connectors are read-only).
- Every action is written to the audit trail with a timestamp.
- If Gemini fails on a demo story, the app falls back to cached output and logs it. Imported stories show an error instead of invented results.

## Problem statement coverage
| Need | Where it is met |
|---|---|
| Fragmented context | Jira story and ranked Confluence passages in one record, each with origin, version, date |
| Gaps and contradictions | Findings with severity, confidence and cited excerpts |
| Clarification overhead | One drafted question per finding, approval queue, typed answers kept as decisions |
| Traceability | Criterion-to-evidence matrix with supported, no evidence, conflicting, unknown |
| Documentation effort | Markdown draft with an AI summary (when live), decisions and open items |
| Trust and governance | Validation, human approval, audit trail, demo versus live labels |
| Measurable value | Evaluation tab: precision, recall, evidence validity, time |

## Known limits
- Retrieval is keyword ranking over at most 5 Confluence pages and 8 passages, not semantic search.
- Acceptance criteria are parsed by a heuristic and need a recognisable section in the Jira description.
- No code, test or CI connectors: diffs and test runs exist only as demo fixtures, so traceability on imported stories usually reports no evidence until those sources exist.
- No write-back to Jira or Confluence, and no activity or timesheet features.
- The evaluation set is tiny and synthetic. Measure real stories before claiming performance.
- No user login in the app itself. Protect it with Cloud Run's private access or IAP.
