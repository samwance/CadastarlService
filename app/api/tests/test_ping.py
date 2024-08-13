import pytest

from app.api.tests.conftest import client


@pytest.mark.asyncio
async def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}