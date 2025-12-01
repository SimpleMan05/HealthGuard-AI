from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RemedyRequest(BaseModel):
    issue: str

class RemedyResponse(BaseModel):
    remedy: str


HOME_REMEDIES = {
    "cold": "Drink warm fluids, inhale steam, rest well, and use saline drops for congestion.",
    "fever": "Stay hydrated, take light meals, rest, and use a cool compress on your forehead.",
    "cough": "Take warm honey water, inhale steam, avoid cold drinks, and rest your throat.",
    "headache": "Drink water, rest in a dark quiet room, and gently massage your temples.",
    "stomach pain": "Drink warm water, avoid heavy meals, and try ginger tea.",
    "sore throat": "Gargle with warm salt water, drink warm liquids, and avoid cold foods."
}


@router.post("/home_remedy", response_model=RemedyResponse)
def home_remedy(data: RemedyRequest):

    issue = data.issue.lower()

    for key in HOME_REMEDIES:
        if key in issue:
            return RemedyResponse(remedy=HOME_REMEDIES[key])

    return RemedyResponse(
        remedy="No specific home remedy found. Please monitor symptoms or consult a doctor if needed."
    )
