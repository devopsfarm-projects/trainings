# Module 01 — Introduction & Foundations

Duration: 15 min theory / 45 min hands-on (total 60 min)

Slide outline / speaker notes

- Title slide: "AI in DevOps — what, why, when"
- Learning objectives (1 slide):
  - Understand LLM capabilities and limits
  - Recognize common failure modes (hallucination, bias, stale data)
  - Know basic human-in-the-loop patterns
- Key concepts (2–3 slides):
  - What is an LLM? (brief non-deep-dive)
  - Prompt → Response: determinism vs randomness
  - Safety concerns: PII, secrets, hallucinations
- Patterns (2 slides):
  - Suggest-only vs apply modes
  - Human approval gates; auditable actions
- Diagram (1 slide): Typical DevOps pipeline with AI overlay
  - CI/CD, Monitoring, ChatOps boxes; arrows showing LLM-assisted steps
- Quick demo outline (1 slide): Lab 01 prompt → validator

Speaker notes
- Emphasize examples (e.g., changelog generation, test suggestion) rather than internals.
- Show a short bad output and explain why validation is necessary.
