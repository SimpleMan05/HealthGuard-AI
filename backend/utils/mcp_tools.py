import json
from pathlib import Path

# ---- TOOL 1: Load symptom rules from JSON ----
def load_symptom_rules():
    try:
        file_path = Path(__file__).parent.parent / "model" / "symptom_rules.json"
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": f"Failed to load symptom rules: {e}"}


# ---- TOOL 2: Simple emergency guideline retriever ----
def get_emergency_guideline(symptom):
    guidelines = {
        "fever": "If fever is above 103°F or persists more than 3 days, seek medical attention.",
        "chest pain": "Chest pain can indicate cardiac emergency. Seek urgent care.",
        "breathing": "Difficulty breathing is a medical emergency. Contact emergency services."
    }

    for key in guidelines:
        if key in symptom.lower():
            return guidelines[key]

    return "No emergency guideline available for this symptom."


# ---- TOOL 3: Basic home remedy recommender ----
def get_home_remedy(symptom):
    remedies = {
        "cough": "Drink warm water and honey. Avoid cold drinks.",
        "fever": "Stay hydrated, rest, and use cold compress.",
        "headache": "Reduce screen time, hydrate, and rest in a dark room."
    }

    for key in remedies:
        if key in symptom.lower():
            return remedies[key]

    return "No home remedy available. Provide more details."
