from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmergencyRequest(BaseModel):
    symptoms: list[str]

class EmergencyResponse(BaseModel):
    level: str  # "emergency", "urgent", "home_care"
    advice: str

@router.post("/classify_emergency", response_model=EmergencyResponse)
def classify_emergency(data: EmergencyRequest):

    symptoms = [s.lower() for s in data.symptoms]

    # --- EMERGENCY CONDITIONS ---
    emergency_keywords = [
        "chest pain", "severe bleeding", "unconscious",
        "difficulty breathing", "no pulse", "heart attack",
        "stroke", "seizure"
    ]

    for keyword in emergency_keywords:
        if keyword in " ".join(symptoms):
            return EmergencyResponse(
                level="emergency",
                advice="This situation appears critical. Seek immediate medical help or call emergency services."
            )

    # --- URGENT CARE CONDITIONS ---
    urgent_keywords = [
        "high fever", "severe headache", "vomiting", "fracture",
        "dizziness", "persistent pain"
    ]

    for keyword in urgent_keywords:
        if keyword in " ".join(symptoms):
            return EmergencyResponse(
                level="urgent",
                advice="This seems urgent. Please visit a doctor within the next few hours."
            )

    # --- HOME CARE ---
    return EmergencyResponse(
        level="home_care",
        advice="Symptoms appear mild. You may follow home-care instructions or monitor for changes."
    )
