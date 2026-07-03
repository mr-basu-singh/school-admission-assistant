import os
import sys

# Add the project root to Python's import path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "School Admission Assistant API Running"


def test_ask():
    response = client.post(
        "/ask",
        json={
            "question": "What is the admission process?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data