# Sprachly 💬

An AI-powered language tutor. Chat with **Maxin** in English or German — he detects your language automatically and responds like a real friend, not a textbook.

> Still in progress 🚧

## Demo
🔗 [sprachlytutor.vercel.app](https://sprachlytutor.vercel.app)

## Stack

| Layer | Tech |
|-------|------|
| Frontend | HTML / CSS / JS |
| Backend | FastAPI (Python) |
| AI | Groq — LLaMA 3.3 70B |
| Deploy | Vercel (frontend) + Render (backend) |

## Features
- Auto-detects English or German and responds in the same language
- Corrects mistakes casually, like a friend would
- Matches your level — beginner or advanced
- Short, natural replies — no essays, no bullet points

## Run locally

```bash
# backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# add your key
echo "GROQ_API_KEY=your_key_here" > .env
```

## Built by
[Nadine Jemaa](https://github.com/NadineNJ) — software engineering student
