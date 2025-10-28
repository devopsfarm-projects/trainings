# Lab 02 — LLMs in CI/CD: Changelog generation and safe commits

Duration: 90 minutes

Prerequisites: GitHub repo (can be local), `node` or `python`, familiarity with GitHub Actions

Goal: Add a safe LLM step to a CI pipeline which generates a `CHANGELOG.md` from commit messages and opens a PR with the changelog.

Setup
- Ensure `GITHUB_TOKEN` (or a test token) is configured in your environment or use a mocked flow.

Exercises
1. Inspect `starter/.github/workflows/changelog.yml` (provided) and run it locally via `act` or push to a test repo.
2. Implement guardrails: only run on release branches, and redact tokens from outputs.
3. Add a unit test that asserts the generated changelog contains expected commit titles and no secrets.

Deliverable
- A PR in the test repo that contains the generated `CHANGELOG.md` or a local run log demonstrating the flow.

Files
- `starter/` — workflow template and sample action that calls an LLM (mockable)
- `solution/` — reference action and tests
- `tests/` — automated tests to validate outputs
