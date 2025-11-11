import pandas as pd

df = pd.read_csv("md.csv")

def assess_patient_symptoms(symptoms):
    user_symptoms = [s.strip().lower() for s in symptoms.split(",") if s.strip()]
    if not user_symptoms:
        return "No symptoms provided."

    matches = []
    for _, row in df.iterrows():
        csv_symptoms = [s.strip().lower() for s in str(row["Symptoms"]).split(",")]
        overlap = len(set(user_symptoms) & set(csv_symptoms))
        if overlap > 0:
            jaccard = overlap / (len(user_symptoms) + len(csv_symptoms) - overlap)
            confidence = round(jaccard * 100, 1)
            matches.append({
                "Disease": row["Disease"],
                "Advice": row["Advice"],
                "Severity": row["Severity"],
                "Confidence": confidence
            })

    if not matches:
        return "No matching disease found."

    matches.sort(key=lambda x: x["Confidence"], reverse=True)
    return matches[:3]
