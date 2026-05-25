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

## Deployment

### Backend → Render.com
1. Push to GitHub
2. Create new Web Service on render.com
3. Connect your repo, set root to `backend/`
4. Add environment variable: `GROQ_API_KEY` = your key
5. Copy the Render URL (e.g. `https://sprachly-backend.onrender.com`)

### Frontend → Vercel
1. Update `API_URL` in `test_ui/index.html` to your Render backend URL
2. Deploy `test_ui/` folder to Vercel

## Adding a New Language
Edit `backend/services/prompts.py` and add a new entry to `LANGUAGE_PROMPTS`.
