from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SymptomInput(BaseModel):
    symptoms: str


class SymptomOutput(BaseModel):
    condition: str
    recommendation: str


# -------------------------
# RULE-BASED SYMPTOM ENGINE
# -------------------------

RULES = [
    {
        "keywords": ["fever", "cough", "cold", "sore throat"],
        "condition": "Common Flu",
        "recommendation": "Rest well, stay hydrated, monitor temperature, and use home remedies. Consult a doctor if fever persists for more than 3 days."
    },
    {
        "keywords": ["chest pain", "breath", "breathing difficulty"],
        "condition": "Possible Cardiac / Respiratory Issue",
        "recommendation": "This may be serious. Seek emergency medical attention immediately."
    },
    {
        "keywords": ["headache", "nausea", "light sensitivity"],
        "condition": "Possible Migraine",
        "recommendation": "Rest in a dark room, stay hydrated, and avoid triggers. Consult a doctor if headaches persist."
    },
    {
        "keywords": ["stomach pain", "diarrhea", "loose motion"],
        "condition": "Stomach Infection",
        "recommendation": "Stay hydrated, avoid spicy food, and use ORS. Seek care if symptoms persist."
    },
    {
        "keywords": ["rash", "itching", "redness"],
        "condition": "Allergic Reaction",
        "recommendation": "Avoid allergens, use soothing lotion. See a doctor if swelling or breathing difficulty occurs."
    }
]


@router.post("/symptom_rules", response_model=SymptomOutput)
def analyze_symptoms(data: SymptomInput):

    text = data.symptoms.lower()

    for rule in RULES:
        if any(keyword in text for keyword in rule["keywords"]):
            return SymptomOutput(
                condition=rule["condition"],
                recommendation=rule["recommendation"]
            )

    return SymptomOutput(
        condition="Not Identified",
        recommendation="No clear match found. Describe symptoms in more detail or consult a professional."
    )
