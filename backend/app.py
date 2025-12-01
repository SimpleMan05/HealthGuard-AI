from fastapi import FastAPI
from pydantic import BaseModel
from agent import health_agent

app = FastAPI(title="HealthGuard-AI", version="1.0.0")

# --- Request Schema ---
class SymptomRequest(BaseModel):
    symptom: str

# --- Root Endpoint ---
@app.get("/")
def home():
    return {
        "message": "HealthGuard-AI is running",
        "status": "ok"
    }

# --- Agent Endpoint ---
@app.post("/analyze")
async def analyze_symptom(payload: SymptomRequest):
    result = await health_agent.run({"symptom": payload.symptom})
    return result
