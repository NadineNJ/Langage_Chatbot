# Sprachly 💬

AI-powered language tutor. Chat with Max in English or German — he auto-detects your language and responds accordingly.

## Stack
- **Frontend:** HTML/CSS/JS → deployed on Vercel
- **Backend:** FastAPI (Python) → deployed on Render
- **AI:** Groq (LLaMA 3.3 70B) — free

## Local Development

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
# Add your GROQ_API_KEY to backend/.env
uvicorn main:app --reload
```

### Frontend
```bash
cd test_ui
npx serve .
# Open http://localhost:3000
```

