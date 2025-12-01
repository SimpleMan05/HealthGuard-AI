def analyze_basic_symptoms(symptom):
    symptom = symptom.lower()

    if "fever" in symptom:
        return "Possible fever detected. Check temperature, hydrate, and rest."
    if "cough" in symptom:
        return "Persistent cough noted. Could be viral infection or irritation."
    if "headache" in symptom:
        return "Headache detected. Ensure hydration; observe stress or screen-time."

    return "Symptom not recognized. Provide more details."
