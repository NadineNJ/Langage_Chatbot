from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.agent import get_agent_response
import traceback

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    language: str = "german"
    conversation_history: list = []


class ChatResponse(BaseModel):
    reply: str
    language: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        reply = await get_agent_response(
            message=request.message,
            language=request.language,
            history=request.conversation_history,
        )
        return ChatResponse(reply=reply, language=request.language)
    except Exception as e:
        traceback.print_exc()  # prints full error in uvicorn terminal
        raise HTTPException(status_code=500, detail=str(e))
