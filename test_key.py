import os
from groq import Groq

api = os.getenv("GROQ_API_KEY")
print("KEY:", api)

client = Groq(api_key=api)

resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Hello!"},
    ],
)

print("AI:", resp.choices[0].message.content)
