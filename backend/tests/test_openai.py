import pytest
from unittest.mock import patch
from app.services.ai_service import AIService

@pytest.fixture
def mock_openai_api_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-api-key")

def test_analyze_text_success(mock_openai_api_key):
    # Mock the OpenAI response
    with patch('openai.Completion.create') as mock_create:
        mock_create.return_value = {
            "choices": [{
                "text": "Test response"
            }]
        }

        ai_service = AIService()
        result = ai_service.analyze_text("Test input")

        mock_create.assert_called_once_with(
            engine="text-davinci-003",
            prompt="Test input",
            max_tokens=150
        )

        assert result == "Test response"
