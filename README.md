🩺 Medical Symptom Checker

An AI-powered interactive health assistant built using Streamlit

✅ Overview

This project is an end-to-end, user-facing medical symptom checker that helps users understand possible health conditions based on the symptoms they enter. The system combines a structured medical dataset with a lightweight AI explanation generator to provide a user-friendly diagnostic experience.

Users can:

a) Select symptoms through checkboxes
b) Enter symptoms manually
c) Chat with the HealthBot
d) Receive top 3 possible disease matches
e) View severity level, advice, and confidence score
f) Read simplified AI-generated explanations
g) Access the deployed web app online

✅ Problem Statement

People often search online for symptoms and get overwhelmed or misled by scattered information. There is a need for a simple, interactive tool that helps users make sense of symptoms quickly and safely.

This application helps users:

Understand possible conditions

a) Get basic health guidance
b) Learn when to seek medical help
c) Interact with an AI assistant in real time
d) Target users include students, general public, and anyone seeking quick preliminary information.

✅ Dataset

A custom medical dataset (md.csv) was created containing:

a) Disease name
b) Symptoms list
c) Medical advice
d) Severity (Mild / Moderate / Severe)

The system matches user symptoms against this dataset using overlap scoring.

✅ Features
🔹 1. Symptom-Based Diagnosis

Users enter symptoms manually or via checkboxes
System calculates symptom overlap
Displays Top 3 matches (“Differential Diagnosis”)

Each includes:

✅ Disease

✅ Severity level

✅ Medical advice

✅ Confidence score

🔹 2. AI Explanation

The app uses a lightweight OpenAI API call to generate:

Simple explanations of the disease
Why symptoms match
What the user should understand

(If no key is provided, the system still works using CSV-based results.)

🔹 3. Chatbot Mode

Users can chat with HealthBot, entering symptoms conversationally.
The chatbot responds with:

Matching conditions
Confidence
Severity
Advice
AI-generated explanation

🔹 4. UI/UX Enhancements

Gradient background
Card-style disease display
Emojis for severity
Randomized health tips
Clean and beginner-friendly interaction flow

✅ Technical Stack

🖥️ Frontend / UI

Streamlit
Custom HTML/CSS for styling

⚙️ Backend

Python
Pandas (CSV handling)
Custom matching algorithm

🤖 AI Integration

OpenAI API (Chat Completions → updated to new API syntax)

📦 Deployment

Streamlit Cloud
GitHub version control

✅ System Architecture
User Input → Streamlit UI → Symptom Processor → 
CSV Matching Engine → Top 3 Predictions → AI Summarizer → Output to UI

✅ Run the App Locally

1) Clone the repository:

git clone https://github.com/Khushi0418/medical_symptom_checker.git
cd medical_symptom_checker


2) Create a virtual environment:

python -m venv venv
venv\Scripts\activate


3) Install dependencies:

pip install -r requirements.txt


4) Run the app:

streamlit run app.py

✅ Deployed App

🔗 Live Streamlit App:
https://medicalsymptomchecker-cffcvjylh83shgtskjtzr9.streamlit.app/

(Replace with your actual URL)

✅ Evaluation Summary

a) Users tested the system; feedback was positive regarding clarity and UI.
b) Responses are fast (usually under 3 seconds).
c) Diagnosis accuracy is reasonable for educational use.
d) AI explanation improves user understanding.

✅ Future Improvements

Add more diseases to the dataset
Introduce a trained ML model instead of rule-based matching
Use embeddings for better symptom mapping
Add multilingual support
Add secure user accounts for history tracking

✅ License

This project is for educational purposes only and not a replacement for professional medical diagnosis.
