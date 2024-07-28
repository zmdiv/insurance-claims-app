import openai
from ..core.config import settings

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def analyze_text(self, text: str, question: str) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{text}\n\n{question}",
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return str(e)
