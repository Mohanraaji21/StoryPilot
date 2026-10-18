# StoryPilot

**Turn scattered engineering context into evidence-linked briefs, clear requirement gaps, and review-ready documentation.**

StoryPilot is an AI co-pilot for software teams. It brings a Jira story and relevant Confluence information together, helps identify missing or conflicting requirements, and maps acceptance criteria to the evidence provided. The goal is to make it easier for teams to understand a story before implementation and keep its supporting decisions and documentation traceable.

## What it does

- Imports Jira issues and searches Confluence for related pages.
- Parses acceptance criteria from the Jira description.
- Uses Gemini on Vertex AI to analyze supplied story context.
- Shows findings with source references and exact evidence excerpts.
- Builds a criterion-to-evidence traceability view.
- Drafts completion documentation from the story, analysis, and recorded decisions.
- Provides an approval queue and audit trail for review.
- Supports a seeded demo flow and evaluation metrics.

## How it works

1. Import a Jira story and retrieve relevant Confluence passages.
2. Analyze the story and its supplied sources.
3. Review evidence-linked findings and clarification questions.
4. Record decisions and inspect acceptance-criteria traceability.
5. Generate, review, and export a Markdown documentation draft.

## Built with

- **Backend:** Python, FastAPI
- **Frontend:** React
- **AI:** Gemini through Vertex AI
- **Storage:** Firestore, with local JSON fallback for development
- **Deployment:** Google Cloud Run

## Designed for trust

StoryPilot treats imported source text as untrusted data. Findings are checked against the loaded sources, and findings without valid evidence are discarded. Generated questions and documentation are presented for human review. Jira and Confluence integrations are read-only; StoryPilot does not post changes back to Atlassian.

## Current scope

Confluence retrieval uses keyword search and is limited to a small number of pages and passages. Acceptance criteria are extracted heuristically from a recognizable section in the Jira description. The current app does not connect to code repositories, pull requests, CI, or test systems, so imported stories may have limited implementation evidence. Evaluation data is small and synthetic; results should not be treated as proof of production performance.

## Getting started

See [`docs/SETUP_GUIDE.md`](docs/SETUP_GUIDE.md) for local setup, Atlassian and Google Cloud configuration, and Cloud Run deployment. Keep credentials in environment configuration or Secret Manager—never commit tokens or `.env` files.
