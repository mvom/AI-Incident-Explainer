import pytest
from app.rag import pipeline

def test_answer_question():
    result = pipeline.answer_question("What is an incident?")
    assert isinstance(result, str)
    assert len(result) > 0
