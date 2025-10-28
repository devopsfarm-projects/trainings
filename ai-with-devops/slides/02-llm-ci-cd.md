# Module 02 — LLMs in CI/CD & Prompt Engineering

Duration: 30 min theory / 90 min hands-on (total 120 min)

Slide outline / speaker notes

- Title slide: "Putting LLMs in the pipeline"
- Where to integrate LLMs (1 slide): pre-commit, CI steps, release hooks, bots
- Tradeoffs (2 slides): latency, cost, reproducibility, idempotency
- Prompt engineering best-practices (3 slides):
  - Templates, system messages, few-shot examples, temperature & max tokens
  - Prompt caching and canonicalization for reproducibility
- Guardrails (2 slides):
  - Input sanitization, output validators, redaction of PII/secrets
  - Approve vs auto-apply modes, audit logs
- Example workflows (2 slides):
  - Changelog generation (Lab 02)
  - Auto-generated tests (Lab 04)
- Demo notes: show `changelog_gen.py` (mock) and explain tests

Speaker notes
- Show prompt examples and explain how small wording changes affect outputs.
- Discuss how to write unit tests for LLM outputs (string heuristics, regex checks).
