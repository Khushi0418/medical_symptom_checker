import pandas as pd

df = pd.read_csv("md.csv", sep=",", quotechar='"', engine="python")

def assess_patient_symptoms(user_input):
    user_input = user_input.lower()
    user_symptoms = [s.strip() for s in user_input.split(",")]

    possible_diseases = []
    for idx, row in df.iterrows():
        csv_symptoms = [s.strip().lower() for s in str(row["Symptoms"]).split(",")]
        overlap = len(set(user_symptoms) & set(csv_symptoms))
        if overlap > 0:
           
            confidence = overlap / (len(user_symptoms) + len(csv_symptoms) - overlap) * 100
            possible_diseases.append({
                "Disease": row["Disease"],
                "Advice": row["Advice"],
                "Severity": row["Severity"],
                "Confidence": confidence
            })

    possible_diseases.sort(key=lambda x: x["Confidence"], reverse=True)
    top_3 = possible_diseases[:3]

    if not top_3:
        return "No matching disease found."

    return top_3
