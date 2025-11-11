from groq import Groq
import os

def generate_ai_response(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "AI unavailable (Missing API key)."

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI unavailable (Error code: {e})"
