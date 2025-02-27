import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_german_response(message: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",  # or GPT-4 if you have access
        prompt=f"Translate and respond in German: {message}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
