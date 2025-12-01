from fastapi import FastAPI
from pydantic import BaseModel
from agent import health_agent

from tools.emergency_tool import router as emergency_router
from tools.home_remedy_tool import router as home_remedy_router
from tools.symptom_rules_tool import router as symptom_rules_router
from agents.triage_agent import router as triage_agent_router
from frontend.chat_api import router as chat_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="HealthGuard-AI", version="1.0.0")

app.include_router(emergency_router, prefix="/tools", tags=["emergency"])
app.include_router(home_remedy_router, prefix="/tools", tags=["home_remedy"])
app.include_router(symptom_rules_router, prefix="/tools", tags=["symptom_rules"])
app.include_router(triage_agent_router, prefix="/agent", tags=["agent"])
app.include_router(chat_router, prefix="/frontend", tags=["chat"])


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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)