# This course targets use of AI in devops workflow.

# Use of AI in DevOps Workflows — Course repo

This repository contains materials for the 10–12 hour course "Use of AI in DevOps Workflows" — a mix of short theory and mostly hands-on labs.

Structure
- `setup.sh` — quick environment checker and bootstrap
- `secrets.example` — names of environment variables used by labs (never store real keys)
- `slides/` — slide decks and outlines for instructors
- `labs/` — per-module lab folders (01..06)
- `ci-examples/` — small GitHub Actions examples used in labs
- `instructor-notes/` — rubrics, troubleshooting, and delivery guides

How to use
1. Run `./setup.sh` to validate the environment and install tooling. (It will not store credentials.)
2. Pick a lab under `labs/` and follow its `README.md`.
3. For CI examples see `ci-examples/github-actions/`.

If you want me to add slide decks or generate starter code for a specific lab, reply with which module to prioritize (e.g., "Lab 02 - CI/CD").

Course authors / maintainer notes
- Keep real API keys out of this repository. Use GitHub Secrets or local environment variables as documented in `secrets.example`.
- Starter solutions live in each lab's `solution/` directory or a separate branch if needed.

Enjoy teaching!

