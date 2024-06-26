from typing import Callable
from fastapi.testclient import TestClient
from fastapi import status


def test_create_new_permission(client: TestClient):
    response = client.post(
        url="/permissions",
        json={"name": "new permission", "description": "some description"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "new permission"


def test_can_not_create_same_permission_twice(client: TestClient, add_permission):
    add_permission()
    response = client.post(
        url="/permissions",
        json={
            "name": "Permission to duplicate",
            "description": "A permission"
        }
    )
    assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE


def test_get_all_permissions(client: TestClient, add_permission):
    add_permission()
    response = client.get("/permissions")

    assert len(response.json()) == 1


def test_get_permission_by_id(client: TestClient, add_permission: Callable):
    add_permission()

    response = client.get(
        url="/permissions/1"
    )

    assert response.json()["id"] == 1
    assert response.json()["name"] == "Permission to duplicate"
