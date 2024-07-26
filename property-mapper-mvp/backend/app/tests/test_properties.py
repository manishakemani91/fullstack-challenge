import pytest
import os
from fastapi.testclient import TestClient
from app.main import app  
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
from dotenv import load_dotenv
from app.core.db.mock_session import engine, test_client

load_dotenv(".env")

# It drops everything from the db and then recreate each time tests runs
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = test_client()

@pytest.fixture
def test_bad_request_field():
    response = client.get("/autocomplete", params={"query": "test", "field": "invalid_field"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid field"}

def test_empty_query_string(mock_get_db):
    with patch("app.routers.autocomplete.get_db", mock_get_db):
        mock_get_db.query().filter().limit().offset().all.return_value = []
        response = client.get("/autocomplete", params={"query": "", "field": "full_address"})
        assert response.status_code == 200
        assert response.json() == {"results": [], "hasMore": False}

def test_search_string_no_match(mock_get_db):
    with patch("app.routers.autocomplete.get_db", mock_get_db):
        mock_get_db.query().filter().limit().offset().all.return_value = []
        response = client.get("/autocomplete", params={"query": "nonexistent", "field": "full_address"})
        assert response.status_code == 200
        assert response.json() == {"results": [], "hasMore": False}

def test_search_string_match(mock_get_db):
    with patch("app.routers.autocomplete.get_db", mock_get_db):
        mock_get_db.query().filter().limit().offset().all.return_value = [sample_property]
        response = client.get("/autocomplete", params={"query": "123 Main St", "field": "full_address"})
        assert response.status_code == 200
        assert response.json() == {
            "results": [sample_property],
            "hasMore": False
        }

def test_search_string_partial_match(mock_get_db):
    with patch("app.routers.autocomplete.get_db", mock_get_db):
        mock_get_db.query().filter().limit().offset().all.return_value = [sample_property]
        response = client.get("/autocomplete", params={"query": "Main", "field": "full_address"})
        assert response.status_code == 200
        assert response.json() == {
            "results": [sample_property],
            "hasMore": False
        }

def test_search_string_multiple_results(mock_get_db):
    properties = [sample_property] * 21  # 21 properties to test pagination
    with patch("app.routers.autocomplete.get_db", mock_get_db):
        mock_get_db.query().filter().limit().offset().all.return_value = properties
        response = client.get("/autocomplete", params={"query": "Main", "field": "full_address", "page_size": 20})
        assert response.status_code == 200
        assert len(response.json()["results"]) == 20
        assert response.json()["hasMore"] == True

def test_database_failure(mocker):
    mocker.patch("app.routers.autocomplete.get_db", side_effect=Exception("DB failure"))
    response = client.get("/autocomplete", params={"query": "Main", "field": "full_address"})
    assert response.status_code == 500
    assert response.json() == {"detail": "DB failure"}
