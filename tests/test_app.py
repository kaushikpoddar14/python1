import pytest
from app import app


@pytest.fixture
def client():
    """Flask test client setup"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    """Check karein ki Homepage 200 OK status code de raha hai"""
    response = client.get("/")
    assert response.status_code == 200


def test_home_content_heading(client):
    """Check karein ki page HTML mein 'Hello, World!' ka heading hai"""
    response = client.get("/")
    assert b"Hello, World!" in response.data


def test_home_content_paragraph(client):
    """Check karein ki page HTML mein paragraph text exist karta hai"""
    response = client.get("/")
    assert b"My first Python web app, ready for GitHub." in response.data
