from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import chat

load_dotenv()  # loads OPENAI_API_KEY from .env file

app = FastAPI(title="Language Tutor Agent")

# Allow all origins (update this to your Vercel domain after deployment)
# e.g. allow_origins=["https://sprachly.vercel.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

app.include_router(chat.router, prefix="/api")


@app.get("/")
def root():
    return {"status": "Language Tutor Agent is running"}
