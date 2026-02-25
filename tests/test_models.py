from app.models.schemas import IncidentQuery
import pytest

def test_incident_query_model():
    q = IncidentQuery(question="Test?")
    assert q.question == "Test?"
