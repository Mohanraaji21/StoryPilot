# StoryPilot setup guide (Google Cloud console, Firebase, Gemini, Atlassian)

Your project ID: `storypilot-511912`. Commands are for Windows PowerShell. Replace anything in CAPITALS.

## 0. Prerequisites
- Python 3.12, Node.js 20+, and the Google Cloud CLI (you already have it).
- A Jira Cloud site (and Confluence on the same Atlassian site).

## 1. Confirm the project and billing
1. Open https://console.cloud.google.com and pick `storypilot-511912` in the top project selector.
2. Menu > Billing. The project must be linked to an active billing account, or Vertex AI calls will fail.

## 2. Enable one extra API
Your list already has Vertex AI (`aiplatform`), Firestore, Cloud Run, Cloud Build and Artifact Registry. Add Secret Manager:
1. Menu > APIs & Services > Library > search "Secret Manager API" > Enable.

## 3. Create the Firestore database
1. Menu > Firestore (or open https://console.firebase.google.com, choose the project, then Build > Firestore Database).
2. Click Create database. Edition: Standard. Mode: Native. Location: `asia-south1` (Mumbai) or the region you prefer. The location cannot be changed later.
3. Start in production mode.
4. Open the Rules tab and keep the default deny-all rules. The server uses Google credentials and bypasses rules, and browsers never talk to Firestore directly.
5. After the first run, a `stories` collection appears here. You can inspect every record, including the audit events.

## 4. Choose the Gemini model
1. Menu > Vertex AI > Model Garden > search "Gemini".
2. Open the Flash model you want. I could not verify a model named "3.8 flash", so copy the exact Model ID shown on its card, for example `gemini-x.y-flash`.
3. On the same card, note the supported regions. If `global` is listed, use it. Otherwise use a listed region, such as `us-central1`.
4. These two values go into `GEMINI_MODEL` and `GOOGLE_CLOUD_LOCATION` below.
5. If calls fail with "model not found", the ID or region is wrong, or the model needs access to be enabled on its card.

## 5. Create Atlassian credentials
1. Go to https://id.atlassian.com/manage-profile/security/api-tokens and click Create API token.
2. Name it `storypilot`, set a short expiry, and copy the token immediately.
3. Record both product base URLs. They may be different Atlassian Cloud hosts: Jira might use `https://YOUR-JIRA-SITE.atlassian.net`, while Confluence might use `https://YOUR-CONFLUENCE-SITE.atlassian.net`.
4. The token inherits your account's access. Prefer a dedicated read-only service account that can see only the projects and spaces you want analysed.
5. Jira stories should contain a heading line `Acceptance Criteria` followed by one criterion per line or bullet. Without it, StoryPilot warns and shows no criteria.

## 6. Authenticate on your machine
```powershell
gcloud auth login
gcloud config set project storypilot-511912
gcloud auth application-default login
gcloud auth application-default set-quota-project storypilot-511912
```
Your own account needs the roles `Vertex AI User` and `Cloud Datastore User` (Menu > IAM & Admin > IAM > edit your user). Project Owner already covers both.

## 7. Configure the app
```powershell
cd storypilot\backend
copy .env.example .env
notepad .env
```
Fill in `GEMINI_MODEL`, `GOOGLE_CLOUD_LOCATION`, `ATLASSIAN_JIRA_BASE_URL`, `ATLASSIAN_CONFLUENCE_BASE_URL`, `ATLASSIAN_EMAIL` and `ATLASSIAN_API_TOKEN`. Use the separate Jira and Confluence hosts shown in each product's address bar. The same unscoped API token can be used for both products if the account has access to both. Existing setups using only `ATLASSIAN_BASE_URL` remain supported for sites that share one host. `.env` is git-ignored. Never commit it.

## 8. Run locally
Terminal 1 (API):
```powershell
cd storypilot\backend
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python tests\test_core.py
uvicorn app.main:app --port 8080
```
Terminal 2 (UI):
```powershell
cd storypilot\frontend
npm install
npm run dev
```
Open http://localhost:5173.

## 9. Verify it works
1. The header shows `AI: gemini-live (YOUR-MODEL)`, `Store: firestore`. If it says cached-offline or local-json, a variable or login is missing.
2. On Today, import a real Jira key. Open the story, check the listed sources (Jira plus Confluence parts, each with origin, version and date), then click Analyze story.
3. Answer a question, approve it (the send is simulated), generate and approve the documentation, export Markdown, and check the Evaluation tab.
4. In the Firestore console, confirm the story document exists.

## 10. Deploy to Cloud Run
1. Store the Atlassian token: Menu > Security > Secret Manager > Create secret, name `atlassian-api-token`, paste the token.
2. Menu > IAM & Admin > IAM. Find the Compute Engine default service account (`PROJECTNUMBER-compute@developer.gserviceaccount.com`) and grant: Vertex AI User, Cloud Datastore User, Secret Manager Secret Accessor.
3. From the `storypilot` folder (where the Dockerfile is):
```powershell
gcloud run deploy storypilot --source . --region asia-south1 `
  --set-env-vars GOOGLE_CLOUD_PROJECT=storypilot-511912,GOOGLE_CLOUD_LOCATION=global,GEMINI_MODEL=YOUR-MODEL-ID,ATLASSIAN_JIRA_BASE_URL=https://YOUR-JIRA-SITE.atlassian.net,ATLASSIAN_CONFLUENCE_BASE_URL=https://YOUR-CONFLUENCE-SITE.atlassian.net,ATLASSIAN_EMAIL=you@example.com `
  --set-secrets ATLASSIAN_API_TOKEN=atlassian-api-token:latest
```
4. Cloud Run prints the service URL. Keep the service private (no `--allow-unauthenticated`) when it holds real Jira data, and open it with `gcloud run services proxy storypilot --region asia-south1`. Allow public access only for a demo with synthetic data.
5. To redeploy after changes, run the same command.

## 11. Troubleshooting
| Symptom | Likely cause and fix |
|---|---|
| Header shows cached-offline | `GOOGLE_CLOUD_PROJECT` not set, or `.env` not in `backend/` |
| Analyze returns "Analysis failed" | Wrong model ID or region, missing Vertex AI User role, or billing off |
| Import: HTTP 401 | Wrong email or token, or base URL typo |
| Import: HTTP 403 | The Atlassian account lacks permission. Grant it access to the Jira project/issue or Confluence space. |
| Import: Jira HTTP 404 | Confirm the issue key exists on the configured Jira site (`ATLASSIAN_JIRA_BASE_URL`) and the configured account can browse the project and issue. Jira deliberately uses 404 for both missing and inaccessible issues. The API error message is included when Atlassian provides one. |
| Confluence search skipped warning | Confirm `ATLASSIAN_CONFLUENCE_BASE_URL` matches the Confluence host and the account/token can access Confluence. If authentication succeeds but no pages appear, check page visibility and whether page text matches the Jira story keywords. |
| Store shows local-json | Firestore not created, or ADC login missing. See the console message printed at startup |
| Cloud Run 403 on the URL | The service is private. Use the proxy command above |
