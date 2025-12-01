from fastapi import FastAPI
from agent import health_agent

app = FastAPI()

@app.get("/")
def home():
    return {"status": "HealthGuard-AI backend running"}

@app.post("/analyze")
async def analyze_symptom(payload: dict):
    response = await health_agent.run(payload)
    return {"result": response}
