import pytest
from httpx import AsyncClient

from app.api.tests.conftest import client


@pytest.mark.asyncio
async def test_create_query(ac: AsyncClient):
    query_data = {
        "cadastral_number": "77:01:0004012:2",
        "latitude": 55.755826,
        "longitude": 37.6173
    }
    response = await ac.post("/query", json=query_data)
    assert response.status_code == 200
    query_result = response.json()
    assert query_result["cadastral_number"] == query_data["cadastral_number"]
    assert response.json()["latitude"] == query_data["latitude"]
    assert response.json()["longitude"] == query_data["longitude"]
    assert response.json()["result"] is False

