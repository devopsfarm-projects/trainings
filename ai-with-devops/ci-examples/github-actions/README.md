# CI examples for labs

This folder contains small GitHub Actions examples used by labs. Each example is intentionally minimal and includes a mocked LLM call where appropriate.

Examples
- `changelog-action/` — example Action that generates a `CHANGELOG.md` from commits (Lab 02)
- `test-gen-action/` — example Action that suggests tests and posts comments on PRs (Lab 04)

Guidance
- Do not store provider API keys in these workflows. Use repository secrets or a test mock.
- When demonstrating in class, prefer running locally or in a private test repo.
