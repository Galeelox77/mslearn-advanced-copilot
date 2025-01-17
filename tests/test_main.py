import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_cities_spain():
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "Madrid" in response.json()  # Assuming Madrid is one of the cities in Spain