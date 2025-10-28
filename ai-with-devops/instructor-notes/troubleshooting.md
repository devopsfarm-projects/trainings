# Troubleshooting & common issues

1) Missing dependencies
- Symptom: `./setup.sh` warns about missing tools.
- Fix: Install the missing runtime (python/node/docker) or skip labs that require them.

2) No LLM API key
- Symptom: Calls to LLM fail with authentication error.
- Fix: Use a mock endpoint for class demos or set `OPENAI_API_KEY` in your environment. Never commit keys.

3) CI runs failing due to network or rate limits
- Symptom: Actions fail when calling external APIs.
- Fix: Use cached responses, mock the LLM, or restrict to a small sample dataset for demos.

4) ChatOps action performed an unexpected change
- Symptom: Bot executed an action that changed state.
- Fix: Ensure human approval gates are enabled during demos and tests. Use "dry-run" mode that only prints proposals.

5) Students see hallucinations or incorrect tests
- Symptom: LLM suggests invalid test assertions or incorrect remediation steps.
- Fix: Teach students to treat LLM outputs as suggestions. Add validation tests and require human review before applying.
