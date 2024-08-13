import pytest
from httpx import AsyncClient

from app.api.tests.conftest import client


@pytest.mark.asyncio
async def test_get_history(ac: AsyncClient):
    response = await ac.get("/history")
    assert response.status_code == 200
    history = response.json()
    assert isinstance(history, list)


@pytest.mark.asyncio
async def test_get_history_by_cadastral_number(ac: AsyncClient):
    query_data = {
        "cadastral_number": "77:01:0004012:2",
        "latitude": 55.755826,
        "longitude": 37.6173
    }
    query_response = await ac.post("/query", json=query_data)
    cadastral_number = query_response.json()["cadastral_number"]
    response = await ac.get(f"/history/{cadastral_number}/")
    assert response.status_code == 200
    history = response.json()
    assert isinstance(history, list)
    if history:
        assert response.json()[0]["cadastral_number"] == cadastral_number
