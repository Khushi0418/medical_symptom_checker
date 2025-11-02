import streamlit as st
from query_engine import assess_patient_symptoms
from ai_interface import generate_ai_response
import random

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
div.stButton > button {
    background-color: #1e88e5;
    color: white;
    border-radius: 10px;
    padding: 10px 24px;
    font-size: 16px;
    border: none;
}
div.stButton > button:hover {
    background-color: #1565c0;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
.card {
    border-radius: 15px;
    padding: 15px;
    margin-top: 15px;
    color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}
.mild {
    background: linear-gradient(to right, #66bb6a, #43a047);
}
.moderate {
    background: linear-gradient(to right, #ffb300, #f57c00);
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
                <b>Confidence:</b> {r['Confidence']:.1f}%
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
                f"**{emoji} Disease:** {r['Disease']}\n**Severity:** {r['Severity']}\n**Advice:** {r['Advice']}\n**Confidence:** {r['Confidence']:.1f}%"
            )

        best_match = reply[0]
        summary_prompt = f"Explain in simple terms what {best_match['Disease']} is and why it causes {user_message}."
        summary = generate_ai_response(summary_prompt)
        st.chat_message("assistant").markdown(f"🧠 **AI Explanation:**\n{summary}")
