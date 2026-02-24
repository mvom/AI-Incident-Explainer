# -----------------------------
# API Routes
# -----------------------------
from fastapi import APIRouter
import time
from app.models.schemas import IncidentQuery
from app.rag.pipeline import answer_question

router = APIRouter()

@router.post("/explain-incident")
def explain_incident(query: IncidentQuery):
	"""
	This endpoint exposes the RAG + LLM pipeline as a REST API.
	It takes a user's question, retrieves similar incidents,
	injects context, and generates a human-readable explanation.
	"""
	start_time = time.time()
	response = answer_question(query.question)
	elapsed = round(time.time() - start_time, 2)
	return {
		"question": query.question,
		"explanation": response,
		"answer_time_seconds": elapsed
	}
