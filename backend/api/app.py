from fastapi import FastAPI
from pydantic import BaseModel

from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.sammrize import summarize, generate_title
from core.extrator import (
    extract_actionable_items,
    extract_key_decisions,
    extract_questions
)
from core.rag_engine import build_rag_chain, ask_question

app = FastAPI()


# ---------------- REQUEST MODELS ----------------
class ProcessRequest(BaseModel):
    source: str
    language: str = "en"


class AskRequest(BaseModel):
    transcript: str
    question: str


# ---------------- HEALTH CHECK ----------------
@app.get("/")
def home():
    return {"status": "AI Video Assistant API running"}


# ---------------- MAIN PIPELINE ----------------
@app.post("/process")
def process_pipeline(req: ProcessRequest):

    try:
        # 1. Audio extraction
        processed_audio = process_input(req.source)

        # 2. Transcription
        transcript = transcribe_all(processed_audio, req.language)

        if not transcript or not transcript.strip():
            return {"error": "Empty transcript"}

        # 3. Title
        title = generate_title(transcript)

        # 4. FULL SUMMARY (IMPORTANT)
        video_summary = summarize(transcript)

        # 5. EXTRACTIONS
        actions = extract_actionable_items(transcript)
        decisions = extract_key_decisions(transcript)
        questions = extract_questions(transcript)

        # 6. RAG setup
        rag_chain = build_rag_chain(transcript)

        return {
            "title": title,
            "video_summary": video_summary,   # ⭐ NEW FIELD ADDED
            "transcript": transcript,
            "actions": actions,
            "decisions": decisions,
            "questions": questions,
            "rag_ready": rag_chain is not None
        }

    except Exception as e:
        return {"error": str(e)}


# ---------------- RAG Q/A ----------------
@app.post("/ask")
def ask(req: AskRequest):

    try:
        rag_chain = build_rag_chain(req.transcript)
        answer = ask_question(rag_chain, req.question)

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}