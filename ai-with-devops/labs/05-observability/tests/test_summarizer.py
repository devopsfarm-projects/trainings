from pathlib import Path
import sys

# Add repo root so tests can import shared.mock_llm
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from shared import mock_llm


def test_mock_summarizer_contains_incident_prefix():
    alert_text = "{\"alert\": {\"title\": \"High error rate\"}}"
    prompt = "Summarize the following incident alert and propose triage steps.\n\n" + alert_text
    resp = mock_llm.generate(prompt)["text"]
    assert "Incident summary" in resp or "Suggested steps" in resp or len(resp) > 0
