import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from datetime import datetime

from .main import app

client = TestClient(app)


def test_create_user():
    test_user_data = {"name": "Alice", "email": "Alice@qq.com", "phone": "1334567890"}
    response = client.post("/users/", json=test_user_data)
    assert response.status_code == 200
    assert response.json()["name"] == test_user_data["name"]
    print(response.json())


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(response.json())


def test_read_user():
    response = client.get("/users/2")
    assert response.status_code == 404
    print(response.json())


def test_update_user():
    test_user_data = {"name": "Bob", "email": "Bob@qq.com", "phone": "9876543210", "id": 1, "is_emergency": True}
    response = client.put("/users/", json=test_user_data)
    assert response.status_code == 200
    assert response.json()["name"] == test_user_data["name"]
    print(response.json())


# def test_delete_user():
#     test_user_data = {"name": "Bob", "email": "Bob@qq.com", "phone": "9876543210", "id": 1, "is_emergency": True}
#     response = client.delete("/users/", json=test_user_data)
#     assert response.status_code == 200
#     assert response.json()["name"] == test_user_data["name"]
#     print(f"Deleted user: {response.json()}")


def test_delete_user_by_id():
    response = client.delete("/users/2")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_insert_and_query_with_async():
    time = datetime.now()
    print("start time:", time)
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        for i in range(10000):
            response = await ac.get(url="/users/")
    assert response.status_code == 200
    print(response.json())
    cost_time = datetime.now() - time
    print("end time:", datetime.now())
    print("cost time:", cost_time)


def test_insert_and_query():
    time = datetime.now()
    print("start time:", time)
    for i in range(10000):
        response = client.get("/users/")
        assert response.status_code == 200
        # print(response.json())
    cost_time = datetime.now() - time
    print("end time:", datetime.now())
    print("cost time:", cost_time)
