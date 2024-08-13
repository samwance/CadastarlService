import pytest
from httpx import AsyncClient

from app.api.tests.conftest import client


def test_register():
    response = client.post("/register", json={
        "username": "testuser",
        "password": "testpassword"
    })

    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"


@pytest.mark.asyncio
async def test_login(ac: AsyncClient):
    # Зарегистрируем пользователя
    response = await ac.post("/register", json={
        "username": "loginuser",
        "password": "testpassword"
    })
    assert response.status_code == 201

    # Теперь пытаемся авторизоваться
    response = await ac.post("/login", json={
        "username": "loginuser",
        "password": "testpassword"
    })

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_fail(ac: AsyncClient):
    # Попробуем авторизоваться с неправильным паролем
    response = await ac.post("/login", json={
        "username": "nonexistentuser",
        "password": "wrongpassword"
    })

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

    # Зарегистрируем пользователя
    response = await ac.post("/register", json={
        "username": "testuser_unique",
        "password": "testpassword"
    })
    assert response.status_code == 201

    # Попробуем авторизоваться с неправильным паролем
    response = await ac.post("/login", json={
        "username": "testuser",
        "password": "wrongpassword"
    })

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Incorrect password"
