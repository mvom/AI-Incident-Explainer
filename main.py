from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import IncidentQuery
from app.rag.pipeline import answer_question

# -----------------------------
# Initialize FastAPI app
# -----------------------------
app = FastAPI(title="AI Incident Explainer")

# -----------------------------
# CORS middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# -----------------------------
# Include API routes
# -----------------------------
from app.api.routes import router
app.include_router(router)

# -----------------------------
# Run locally with uvicorn
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)