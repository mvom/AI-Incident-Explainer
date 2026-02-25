from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_e2e_conversation():
    q1 = "How many turbines?"
    r1 = client.post("/explain-incident", json={"question": q1})
    assert r1.status_code == 200
    assert "explanation" in r1.json()
    q2 = "What is the last incident?"
    r2 = client.post("/explain-incident", json={"question": q2})
    assert r2.status_code == 200
    assert "explanation" in r2.json()
