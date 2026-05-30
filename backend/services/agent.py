import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from services.prompts import get_system_prompt

load_dotenv()  # ensure .env is loaded even if called before main.py

def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your_groq_api_key_here":
        raise ValueError("GROQ_API_KEY is not set. Please add your key to backend/.env")
    # Groq is OpenAI-compatible, just different base_url
    return AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )


async def get_agent_response(message: str, language: str, history: list) -> str:
    """
    Sends the user message to OpenAI with the correct language tutor system prompt.
    Maintains conversation history for context.
    """
    client = get_client()  # creates client with validated API key
    system_prompt = get_system_prompt(language)

    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history (last 20 messages to keep context manageable)
    for entry in history[-20:]:
        messages.append({"role": entry["role"], "content": entry["content"]})

    # Add the new user message
    messages.append({"role": "user", "content": message})

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # better at following custom identity/persona
        messages=messages,
        temperature=0.85,
        max_tokens=400,
    )

    return response.choices[0].message.content
