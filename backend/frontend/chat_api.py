from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter()

BASE_URL = "http://localhost:8000/agent/triage"


class ChatInput(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    used_tool: str | None


@router.post("/chat", response_model=ChatResponse)
def chat_interface(data: ChatInput):

    with httpx.Client() as client:
        result = client.post(BASE_URL, json={"query": data.message}).json()

    return ChatResponse(
        reply=result["response"],
        used_tool=result["used_tool"]
    )
