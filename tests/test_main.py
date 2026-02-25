import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_not_found():
    response = client.get("/")
    assert response.status_code == 404

def test_explain_incident():
    response = client.post("/explain-incident", json={"question": "How many turbines?"})
    assert response.status_code == 200
    assert "explanation" in response.json()
