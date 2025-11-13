import os
from groq import Groq

def generate_ai_response(prompt: str) -> str:
    """
    Generate AI explanation for a given symptom or disease using Groq API.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "API key not found. Please configure your GROQ_API_KEY in Streamlit Secrets."

    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ Updated working model
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant that explains diseases and symptoms in simple, educational language."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=250,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI unavailable (Error code: {e})"
