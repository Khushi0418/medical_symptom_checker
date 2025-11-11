from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def normalize_symptoms(text):
    prompt = f"""
    Convert the following symptoms into short, comma-separated medical keywords.
    Do not diagnose. Only rewrite the symptoms into clinical terms.

    Symptoms: "{text}"

    Examples:
    "tired all the time" → "fatigue, weakness"
    "pain behind eyes" → "headache, eye pain"
    "burning in stomach" → "acidity, abdominal pain"

    Now rewrite:
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def generate_ai_response(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content.strip()
