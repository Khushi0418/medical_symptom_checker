import pandas as pd
import os
from groq import Groq

df = pd.read_csv("md.csv")

# ✅ Symptom synonyms dictionary (small but effective)
SYMPTOM_SYNONYMS = {
    "tired": "fatigue",
    "tired all the time": "fatigue",
    "burning sensation": "heartburn",
    "burning in stomach": "heartburn",
    "pain behind eyes": "headache",
    "shaking hands": "tremors",
    "restlessness": "anxiety",
    "loose motion": "diarrhea",
    "stomach pain": "abdominal pain",
    "lower stomach pain": "abdominal pain",
}

# ✅ Clean text
def normalize(text):
    if not isinstance(text, str):
        return ""
    return text.strip().lower()

# ✅ Expand synonym matches
def expand_symptoms(sym_list):
    expanded = []
    for s in sym_list:
        s = normalize(s)
        if s in SYMPTOM_SYNONYMS:
            expanded.append(SYMPTOM_SYNONYMS[s])
        expanded.append(s)
    return expanded

# ✅ MAIN FUNCTION
def assess_patient_symptoms(user_input):
    if not user_input:
        return "Please enter symptoms."

    # user symptoms
    raw_user_symptoms = [normalize(x) for x in user_input.split(",")]
    user_symptoms = expand_symptoms(raw_user_symptoms)

    possible_diseases = []

    for idx, row in df.iterrows():
        csv_symptoms = [normalize(x) for x in str(row["Symptoms"]).split(",")]

        # ✅ partial match scoring
        overlap = 0
        for u in user_symptoms:
            for c in csv_symptoms:
                if u in c or c in u:  # substring match
                    overlap += 1

        # ✅ ignore diseases with zero scoring
        if overlap == 0:
            continue

        # confidence based on Jaccard similarity
        confidence = overlap / (len(set(user_symptoms)) + len(set(csv_symptoms)) - overlap) * 100

        possible_diseases.append({
            "Disease": row["Disease"],
            "Symptoms": row["Symptoms"],
            "Advice": row["Advice"],
            "Severity": row["Severity"],
            "Confidence": round(confidence, 1)
        })

    # ✅ If CSV fails completely → fallback to AI
    if not possible_diseases:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "No matching disease found."

        try:
            client = Groq(api_key=api_key)
            resp = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a medical symptom analysis assistant."},
                    {"role": "user", "content": f"Symptoms: {user_input}. What are possible causes?"}
                ]
            )
            return resp.choices[0].message.content
        
        except Exception as e:
            return f"AI unavailable ({e})"

    possible_diseases.sort(key=lambda x: x["Confidence"], reverse=True)

    return possible_diseases[:3]

