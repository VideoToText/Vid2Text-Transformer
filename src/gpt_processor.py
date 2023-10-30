from decouple import config
import openai

def setup_gpt():
    """
    Initialize the OpenAI GPT API with the key from .env file.
    """
    api_key = config('OPENAI_API_KEY')
    openai.api_key = api_key

def process_text_with_gpt(raw_text):
    """
    Given raw text, use the GPT API to structure and refine it.
    """
    response = openai.Completion.create(
      engine="davinci",
      prompt=raw_text,
      max_tokens=500
    )
    refined_text = response.choices[0].text.strip()
    return refined_text
