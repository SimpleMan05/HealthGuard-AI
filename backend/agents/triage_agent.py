from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter()

# Base URL for internal tool usage
BASE_URL = "http://localhost:8000/tools"


class QueryInput(BaseModel):
    query: str


class QueryOutput(BaseModel):
    response: str
    used_tool: str | None


# Simple in-memory session-based history (MCP-like memory behavior)
MEMORY = {
    "symptoms": []
}


def call_tool(endpoint: str, payload: dict):
    """Helper to call backend tools programmatically."""
    url = f"{BASE_URL}/{endpoint}"
    with httpx.Client() as client:
        r = client.post(url, json=payload)
        return r.json()


@router.post("/triage", response_model=QueryOutput)
def triage_agent(user_input: QueryInput):

    text = user_input.query.lower()
    used_tool = None
    final_response = ""

    # -------------------------
    # 1. Detect if user mentions symptoms
    # -------------------------
    symptom_keywords = ["fever", "cough", "cold", "pain", "headache", "breath", "rash", "throat"]

    if any(kw in text for kw in symptom_keywords):
        MEMORY["symptoms"].append(text)

        result = call_tool(
            "symptom_rules",
            {"symptoms": text}
        )
        final_response = (
            f"**Possible Condition:** {result['condition']}\n"
            f"**Recommendation:** {result['recommendation']}"
        )
        used_tool = "symptom_rules"

    # -------------------------
    # 2. Detect if user wants home remedy
    # -------------------------
    elif "remedy" in text or "home treatment" in text:
        if MEMORY["symptoms"]:
            last_symptom = MEMORY["symptoms"][-1]
            result = call_tool(
                "home_remedy",
                {"issue": last_symptom}
            )
            final_response = (
                f"Based on your earlier symptoms:\n\n"
                f"**Home Remedy:** {result['remedy']}"
            )
            used_tool = "home_remedy"
        else:
            final_response = "Please describe your symptoms first."

    # -------------------------
    # 3. Detect emergency words
    # -------------------------
    elif "emergency" in text or "severe" in text or "urgent" in text:
        result = call_tool(
            "emergency",
            {"description": text}
        )
        final_response = (
            f"🚨 **Emergency Check:**\n{result['advice']}"
        )
        used_tool = "emergency"

    # -------------------------
    # 4. Generic fallback
    # -------------------------
    else:
        final_response = (
            "I'm here to help with symptoms, remedies, or emergency guidance. "
            "Please describe what you're experiencing."
        )

    return QueryOutput(
        response=final_response,
        used_tool=used_tool
    )
