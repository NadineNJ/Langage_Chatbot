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


def is_identity_question(message: str) -> bool:
    keywords = ["who made you", "who built you", "who created you", "who are you", 
                "who developed you", "who made u", "who built u", "who created u"]
    return any(k in message.lower() for k in keywords)


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        print(f"MESSAGE RECEIVED: '{request.message}'")  # add this
        print(f"IS IDENTITY: {is_identity_question(request.message)}")  # add this

        if is_identity_question(request.message):
            return ChatResponse(
                reply="Nadine Jemaa built me — she's a software engineering student who created this as a project 😊",
                language=request.language
            )

        reply = await get_agent_response(
            message=request.message,
            language=request.language,
            history=request.conversation_history,
        )
        return ChatResponse(reply=reply, language=request.language)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))