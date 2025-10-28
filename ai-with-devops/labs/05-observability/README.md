# Lab 05 — Observability & Incident Triage with AI

Duration: 90 minutes

Prerequisites: Basic familiarity with logs/metrics (Prometheus/ELK) and Python/Node

Goal: Build a simple pipeline that ingests sample logs/alerts and uses an LLM to summarize incidents and propose runbook steps.

Exercises
1. Load sample alert payloads located in `starter/sample_alerts/`.
2. Run the summarizer script to generate an incident summary and suggested triage steps.
3. Add a confidence field and a human-approval gate before creating a ticket (e.g., GitHub issue).

Deliverable
- Sample issue or local artifact containing the summary and runbook draft.

Files
- `starter/`, `solution/`, `tests/`
