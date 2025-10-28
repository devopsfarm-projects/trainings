# Module 04 — AI-assisted Testing, Code Gen & PR Workflows

Duration: 30 min theory / 90 min hands-on (total 120 min)

Slide outline / speaker notes

- Title slide: "AI for tests and code reviews"
- Use-cases (1 slide): test generation, PR description generation, reviewer suggestions
- Provenance & licensing (1 slide): code origin, attribution, crafted prompts
- Validation patterns (2 slides): unit tests for model outputs, fuzzing, snapshotting
- Workflow example (2 slides): GitHub Action that comments suggested tests; suggest vs apply modes
- Demo: run `test_suggester.py` and show how CI posts a comment (mocked)

Speaker notes
- Recommend keeping AI output as suggestions unless human-reviewed. Show how to add toggles.
