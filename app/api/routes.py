# -----------------------------
# API Routes
# -----------------------------
from fastapi import APIRouter
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
	response = answer_question(query.question)
	return {
		"question": query.question,
		"explanation": response
	}
