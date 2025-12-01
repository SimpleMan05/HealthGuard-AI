from fastapi import FastAPI
from pydantic import BaseModel
from agent import health_agent

from tools.emergency_tool import router as emergency_router
from tools.home_remedy_tool import router as home_remedy_router

app = FastAPI(title="HealthGuard-AI", version="1.0.0")

app.include_router(emergency_router, prefix="/tools", tags=["emergency"])
app.include_router(home_remedy_router, prefix="/tools", tags=["home_remedy"])


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
