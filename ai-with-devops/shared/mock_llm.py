"""A tiny mock LLM client used by labs when no external API is available.

This intentionally returns deterministic, inspectable outputs so students can
focus on prompt design and validation without needing API keys.
"""
from typing import Dict


def generate(prompt: str, max_tokens: int = 256) -> Dict[str, str]:
    """Return a simple deterministic response based on the prompt content.

    The return value mirrors a minimal subset of real LLM client responses:
    {"text": "..."}
    """
    lower = prompt.lower()
    if "changelog" in lower or "generate changelog" in lower:
        # Simple changelog template
        text = "## Changelog\n\n- feat: add user login flow\n- fix: handle null pointer in payments\n"
    elif "suggest tests" in lower or "generate tests" in lower:
        text = "- test_should_handle_valid_input\n- test_should_reject_invalid_input\n"
    elif "summarize" in lower or "incident" in lower:
        text = "Incident summary: High error rate on /api/payments, likely caused by recent deployment. Suggested steps: rollback, check DB connections."
    else:
        # Echo with a short prefix to make the output obvious
        text = f"MOCK_RESPONSE: {prompt[:120]}"

    return {"text": text}
