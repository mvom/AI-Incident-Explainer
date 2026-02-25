import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_explain_incident_valid():
    response = client.post("/explain-incident", json={"question": "Describe incident."})
    assert response.status_code == 200
    assert "explanation" in response.json()

def test_explain_incident_invalid():
    response = client.post("/explain-incident", json={})
    assert response.status_code == 422
