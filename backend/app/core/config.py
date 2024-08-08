import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
openai.api_key = api_key

# Example function to generate a response using the OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can use other engines like "curie", "babbage", "ada"
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
