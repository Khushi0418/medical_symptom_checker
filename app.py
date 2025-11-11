import streamlit as st
from query_engine import assess_patient_symptoms
from ai_interface import generate_ai_response
import random
import os

st.set_page_config(page_title="Medical Symptom Checker", page_icon="🩺", layout="centered")

page_bg = """
<style>
body {
    background: linear-gradient(to bottom right, #e3f2fd, #bbdefb);
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    color: #0d47a1;
    text-align: center;
}
.card {
    border-radius: 15px;
    padding: 18px;
    margin-top: 15px;
    color: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.18);
}
.mild {
    background: linear-gradient(to right, #6ddf6d, #43a047);
}
.moderate {
    background: linear-gradient(to right, #ffca28, #fb8c00);
}
.severe {
    background: linear-gradient(to right, #ef5350, #c62828);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🩺 Medical Symptom Checker")

age_group = st.selectbox("Select your age group:", ["Child", "Adult", "Elderly"])

common_symptoms = ["Fever", "Cough", "Headache", "Fatigue", "Shortness of breath", "Chest pain", "Nausea"]
st.markdown("### ✅ Select symptoms:")
selected_symptoms = [s for s in common_symptoms if st.checkbox(s)]

manual_input = st.text_input("Or enter your symptoms (comma-separated):")

user_input = ", ".join(selected_symptoms + ([manual_input] if manual_input else []))

if user_input:
    results = assess_patient_symptoms(user_input)

    if isinstance(results, str):
        st.warning(results)
    else:
        st.markdown("### 🧬 Differential Diagnosis (Top 3 Matches)")

        for r in results:
            severity = r["Severity"].lower()
            emoji = "💊"
            if severity == "severe":
                emoji = "⚠️"
            elif severity == "moderate":
                emoji = "🩺"
            elif severity == "mild":
                emoji = "🌿"

            st.markdown(
                f"""
                <div class='card {severity}'>
                    <h4>{emoji} {r['Disease']}</h4>
                    <b>Severity:</b> {r['Severity']}<br>
                    <b>Advice:</b> {r['Advice']}<br>
                    <b>Confidence:</b> {r['Confidence']}%
                </div>
                """,
                unsafe_allow_html=True
            )

            if r["Confidence"] < 40:
                st.warning("⚠️ Moderate confidence result — please consult a doctor.")

        tips = [
            "💧 Stay hydrated throughout the day.",
            "🍎 Eat more fruits and vegetables.",
            "🚶 Exercise for 30 minutes daily.",
            "😴 Sleep at least 7-8 hours per night."
        ]
        st.info(random.choice(tips))

st.markdown("---")

st.markdown("### 💬 Chat with HealthBot")
user_message = st.chat_input("Describe your symptoms here...")

if user_message:
    st.chat_message("user").write(user_message)

    reply = assess_patient_symptoms(user_message)

    if isinstance(reply, str):
        st.chat_message("assistant").write(reply)
    else:
        for r in reply:
            emoji = "💊"
            if r["Severity"].lower() == "severe":
                emoji = "⚠️"
            elif r["Severity"].lower() == "moderate":
                emoji = "🩺"
            elif r["Severity"].lower() == "mild":
                emoji = "🌿"

            st.chat_message("assistant").markdown(
                f"**{emoji} Disease:** {r['Disease']}\n"
                f"**Severity:** {r['Severity']}\n"
                f"**Advice:** {r['Advice']}\n"
                f"**Confidence:** {r['Confidence']}%"
            )

        best = reply[0]
        ai_prompt = f"Explain in simple words what {best['Disease']} is and how it causes {user_message}."

        ai_reply = generate_ai_response(ai_prompt)

        if ai_reply:
            st.chat_message("assistant").markdown(f"🧠 **AI Explanation:**\n{ai_reply}")
        else:
            st.chat_message("assistant").markdown("AI explanation unavailable.")
