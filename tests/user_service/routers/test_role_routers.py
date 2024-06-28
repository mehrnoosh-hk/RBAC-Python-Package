import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "role_name, role_description, role_id",
    [("admin", "admin role", 1), ("user", "user role", 2)],
)
def test_admin_can_create_roles(
    role_name: str, role_description: str, role_id: int, client: TestClient
):
    response = client.post(
        "/roles/",
        json={"name": role_name, "description": role_description},
    )
    assert response.status_code == 201
    assert response.json()["name"] == role_name
    assert response.json()["description"] == role_description


def test_admin_can_not_create_the_same_role_twise(client: TestClient):
    # Create the role admin for first time
    response = client.post(
        "/roles/",
        json={"name": "new admin", "description": "admin role"},
    )
    assert response.status_code == 201
    # Create the role admin for second time
    response = client.post(
        "/roles/",
        json={"name": "new admin", "description": "admin role"},
    )
    assert response.status_code == 406
    assert response.json() == {"error": "Role already exists"}


def test_get_all_roles(client: TestClient, add_roles):
    print("test_get_all_roles")
    add_roles()
    response = client.get("/roles/")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_role_by_id(client: TestClient, add_role):
    add_role({"name": "my_admin", "description": "admin role"})

    response = client.get(url="/roles/1")

    assert response.status_code == 200
    assert response.json()["name"] == "my_admin"
