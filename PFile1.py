import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY") 

if not openai.api_key:
    raise ValueError("OPENAI API key is not set")


def analyze_query(query_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query_text }]
    )
    return response["choices"][0]["message"]["content"]

query_text="What is the capital of France?"
print(analyze_query(query_text))

