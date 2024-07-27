import openai
from ..core.config import settings

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def analyze_text(self, text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=150
        )
        return response.choices[0].text.strip()
