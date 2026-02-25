
# AI Incident Explainer

## Overview
AI Incident Explainer is a full-stack application that leverages Retrieval-Augmented Generation (RAG) to answer questions about industrial incidents using a conversational interface. The backend is built with FastAPI and integrates RAG pipelines, while the frontend provides a user-friendly interface for interaction.

## Features
- Conversational Q&A about industrial incidents
- RAG pipeline for document retrieval and answer generation
- REST API endpoints for incident explanation
- Frontend built with React
- End-to-end and integration tests

## Folder Structure

```
├── app/
│   ├── api/           # API routes
│   ├── models/        # Data schemas
│   ├── rag/           # RAG pipeline, embeddings, retriever, ingestion, query
│   └── config.py      # App configuration
├── data/
│   ├── raw/           # Raw incident data
│   └── processed/     # Processed data and scripts
├── frontend/
│   └── frontend/      # React frontend app
├── scripts/           # Utility scripts
├── tests/             # Test suite (e2e, integration, unit)
├── main.py            # FastAPI app entry point
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker setup
├── docker-compose.yml # Multi-container orchestration
```

## Setup

### Backend
1. Create and activate a Python virtual environment:
	```powershell
	python -m venv .venv
	& .venv\Scripts\Activate.ps1
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Run the FastAPI server:
	```bash
	uvicorn main:app --reload
	```

### Frontend
1. Navigate to `frontend/frontend`:
	```bash
	cd frontend/frontend
	```
2. Install Node.js dependencies:
	```bash
	npm install
	```
3. Start the React development server:
	```bash
	npm start
	```

### Docker
To run the project with Docker Compose:
```bash
docker-compose up --build
```

## Usage
Send POST requests to `/explain-incident` with a JSON body containing a `question` field. Example:
```json
{
  "question": "How many turbines?"
}
```
The response will include an `explanation` field.

## Testing
Run tests from the `tests` folder:
```bash
pytest
```
End-to-end tests use FastAPI's TestClient to simulate API requests and validate responses.

## License
MIT License

## Author
Your Name
