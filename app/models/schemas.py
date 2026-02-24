# -----------------------------
# Input data model
# -----------------------------
from pydantic import BaseModel

class IncidentQuery(BaseModel):
	question: str  # user's question about an incident
