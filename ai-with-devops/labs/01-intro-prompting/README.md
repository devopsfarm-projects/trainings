# Lab 01 — Introduction to Prompting and Safe Outputs

Duration: 45–60 minutes

Prerequisites: `python3`, an API key for an LLM (or a mocked endpoint), basic familiarity with bash

Goal: Learn basic prompt design, inspect LLM outputs for hallucinations, and add simple validation.

Setup
- Copy `../secrets.example` to `.secrets` or set environment vars.
- Activate venv: `source ../.venv/bin/activate` (created by `./setup.sh`).

Exercises
1. Call the provided `starter/prompt_test.py` (or run a small script provided by instructor) to send a short prompt to the LLM and print the output.
2. Inspect the output and write a short validator that rejects outputs containing URLs, private keys, or email addresses.
3. Update prompt with explicit guardrails and re-run until validator passes.

Deliverable
- A short script (`solution/validated_output.txt`) and a 2–3 line note describing a failure mode you observed.

Files
- `starter/` — small script to call the LLM (mockable)
- `solution/` — reference solution
- `tests/` — a small validator harness
