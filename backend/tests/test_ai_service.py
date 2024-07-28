import unittest
from unittest.mock import patch, Mock
from app.services.ai_service import AIService

class TestAIService(unittest.TestCase):
    def setUp(self):
        self.ai_service = AIService()
        self.text = "Sample insurance policy text."
        self.question = "What does the policy cover?"

    @patch('app.services.ai_service.openai.Completion.create')
    def test_analyze_text(self, mock_openai_create):
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].text = "The policy covers health expenses."
        mock_openai_create.return_value = mock_response
        
        response = self.ai_service.analyze_text(self.text, self.question)
        self.assertEqual(response, "The policy covers health expenses.")
        mock_openai_create.assert_called_once_with(
            engine="text-davinci-003",
            prompt=f"{self.text}\n\n{self.question}",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )

if __name__ == "__main__":
    unittest.main()
