# Test generation Action (example)

This folder contains an example workflow and helper script that demonstrates how a CI job
could call an LLM to suggest tests for a PR and post the suggestions as a comment.

Important: This is a classroom demo using `shared/mock_llm.py`. Do not call real LLMs from public repos without proper secrets and guardrails.

Files
- `test-gen-workflow.yml` — example workflow (in parent folder)
- `action/` — (optional) a simple action could wrap `pr_suggester.py`
