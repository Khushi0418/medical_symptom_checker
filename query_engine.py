import pandas as pd

try:
    df = pd.read_csv("md.csv")
except Exception as e:
    print("Error loading dataset:", e)
    df = pd.DataFrame(columns=["Disease", "Symptoms", "Advice", "Severity"])

def assess_patient_symptoms(symptom_input):
    if df.empty:
        return "Dataset not found or empty."

    symptoms = [s.strip().lower() for s in symptom_input.split(",") if s.strip()]
    if not symptoms:
        return "Please enter at least one symptom."

    results = []
    for _, row in df.iterrows():
        disease_symptoms = [s.strip().lower() for s in row["Symptoms"].split(",")]
        match_score = len(set(symptoms) & set(disease_symptoms)) / len(disease_symptoms)
        if match_score > 0:
            results.append({
                "Disease": row["Disease"],
                "Severity": row["Severity"],
                "Advice": row["Advice"],
                "Confidence": match_score * 100
            })

    if not results:
        return "No matching disease found."

    results = sorted(results, key=lambda x: x["Confidence"], reverse=True)[:3]
    return results
