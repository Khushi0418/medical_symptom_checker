🩺 Medical Symptom Checker

An AI-powered interactive health assistant built using Streamlit

✅ Overview

This project is an end-to-end, user-facing medical symptom checker that helps users understand possible health conditions based on symptoms they enter. The system combines a structured medical dataset with a rule-based matching engine and a Groq AI–powered explanation generator to provide a user-friendly diagnostic experience.

Users can:

✔ Select symptoms via checkboxes

✔ Enter symptoms manually

✔ Chat with the HealthBot

✔ Receive top 3 possible disease matches

✔ View severity level, advice, and confidence score

✔ Read simplified AI-generated explanations

✔ Access the deployed web app online

✅ Problem Statement

People often search online for symptoms and get overwhelmed or misled by scattered information.
There is a need for a simple, interactive tool that helps users make sense of symptoms quickly and safely.

This application helps users:

Understand possible conditions

Get basic health guidance

Learn when to seek medical help

Interact with an AI assistant in real time

Target Users → Students, general public, and anyone seeking quick preliminary health information.

✅ Dataset

A custom medical dataset (md.csv) was created containing:

Disease name

Symptoms list

Medical advice

Severity level (Mild / Moderate / Severe)

The system matches user symptoms using a rule-based overlap-scoring algorithm.

✅ Features
🔹 1. Symptom-Based Diagnosis

Users input symptoms (typed or selected)

System compares with CSV dataset

Displays Top 3 differential diagnosis matches
Each includes:
✔ Disease
✔ Severity
✔ Advice
✔ Confidence score

🔹 2. AI Explanation (Groq AI)

The app uses Groq’s LLaMA 3.1 API instead of OpenAI to generate:

Simple explanations of the disease

Why symptoms may be related

Easy-to-understand summaries

💡 If the AI key is not available, the system still works using CSV-based results.

🔹 3. Chatbot Mode

Users can chat with HealthBot, entering symptoms conversationally.
Bot responds with:

Matching conditions

Severity & confidence

Medical advice

AI-generated explanation

🔹 4. UI/UX Enhancements

Modern gradient background

Colored disease cards

Emojis for severity

Randomized health tips

Clean and beginner-friendly layout

✅ Technical Stack
🖥️ Frontend / UI

Streamlit

Custom CSS

⚙️ Backend

Python

Pandas

Custom matching logic

🤖 AI Integration (Updated)

Groq API (LLaMA 3.1 models)

Provides explanations and chatbot responses

Faster inference than OpenAI models

📦 Deployment

Streamlit Cloud

GitHub for version control

✅ System Architecture
User Input
     ↓
Streamlit UI
     ↓
Symptom Processing
     ↓
CSV-Based Matching Engine
     ↓
Top 3 Disease Predictions
     ↓
Groq AI Explanation Module
     ↓
Output to UI (Cards + Chatbot)

✅ Run the App Locally
1. Clone the repository
git clone https://github.com/Khushi0418/medical_symptom_checker.git
cd medical_symptom_checker

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add your Groq API Key

Create a .env file:

GROQ_API_KEY=your_key_here


OR set it using environment variables.

5. Run the app
streamlit run app.py

✅ Deployed App

🔗 Live Streamlit App:
https://medicalsymptomchecker-cffcvjylh83shgtskjtzr9.streamlit.app/

✅ Evaluation Summary

✔ Smooth end-to-end workflow

✔ Fast responses (3–5 seconds)

✔ Positive feedback from test users

✔ Stable predictions from CSV + AI hybrid system

✔ AI explanations enhance learning and clarity

✅ Future Improvements

Add a larger medical dataset

Integrate embeddings for better symptom understanding

Use an ML-trained classifier instead of rule-based matching

Add multilingual output

Add user accounts with medical history

Voice-based symptom input

More advanced medical triaging

⚠️ License

This project is for educational purposes only and not a medical diagnostic tool.
Users must consult qualified healthcare professionals for actual medical issues.


