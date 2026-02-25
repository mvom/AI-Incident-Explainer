from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_full_flow():
    question = "What incidents happened?"
    response = client.post("/explain-incident", json={"question": question})
    assert response.status_code == 200
    data = response.json()
    assert data["question"] == question
    assert isinstance(data["explanation"], str)
    assert len(data["explanation"]) > 0
