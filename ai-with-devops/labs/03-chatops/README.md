# Lab 03 — ChatOps: Controlled automation with human-in-the-loop

Duration: 90 minutes

Prerequisites: Node.js or Python for a small webhook server, Slack or a mocked chat interface

Goal: Build a minimal ChatOps flow that converts a natural language request into a safe plan and requires human approval before taking action.

Exercises
1. Run the starter bot and send a request like "Deploy service X to staging".
2. Inspect the bot's proposed plan (manifest diff) and add an approval step that requires a human response.
3. Make the action idempotent and add logging/audit of commands and approvals.

Deliverable
- A demo showing request → proposed plan → approval → (mocked) action.

Files
- `starter/` — minimal bot and mock approval handler
- `solution/` — reference implementation and tests
