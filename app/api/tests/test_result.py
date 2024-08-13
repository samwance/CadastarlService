import pytest
from httpx import AsyncClient

from app.api.tests.conftest import client


@pytest.mark.asyncio
async def test_send_result(ac: AsyncClient):
    # Предварительно создаем запрос
    query_data = {
        "cadastral_number": "77:01:0004012:2",
        "latitude": 55.755826,
        "longitude": 37.6173
    }

    query_response = await ac.post("/query", json=query_data)
    assert query_response.status_code == 200  # Убедитесь, что запрос был успешно создан
    query_id = query_response.json()["id"]
    response = await ac.post(f"/result/{query_id}/")
    assert response.status_code == 200

    # Проверяем историю запросов по кадастровому номеру
    history_response = await ac.get(f"/history/{query_data['cadastral_number']}/")
    assert history_response.status_code == 200
