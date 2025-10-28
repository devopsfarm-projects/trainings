# Lab 04 — AI-assisted testing and PR workflows

Duration: 90 minutes

Prerequisites: Basic repo with a small function to test, GitHub Actions familiarity

Goal: Use an LLM to suggest unit tests for a function, integrate the suggestions into CI in "suggest" mode, and review before applying.

Exercises
1. Run the test-suggestion script against a small Python/JS function.
2. Create a GitHub Action that posts suggested tests as a comment on a PR (do not auto-commit in suggest mode).
3. Add an "apply" toggle to have the action open a PR that adds tests automatically (for instructor demo only).

Deliverable
- A PR or a local run log with suggested tests and a short reflection on false positives/incorrect suggestions.

Files
- `starter/`, `solution/`, `tests/`
