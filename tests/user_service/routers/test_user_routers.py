from fastapi import status
from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    data_dict={
            "email": "test_user@test_domain.com",
            "username": "test_user",
            "password": "test_password",
            "enabled": True,
        }
    response = client.post(
        url="/users/",
        json=data_dict
    )
    assert response.status_code == 201
    assert response.json() == {"username": "test_user"}

    response = client.get("/users/")
    assert response.status_code == 200

    assert len(response.json()) == 1
    assert response.json()[0]["username"] == "test_user"


def test_can_not_create_a_user_with_same_email(client: TestClient, add_user):
    add_user(
        {
            "email": "test_user@test_domain.com",
            "username": "test_user",
            "password": "test_password",
        }
    )

    data_dict = {
            "email": "test_user@test_domain.com",
            "username": "test_user",
            "password": "test_password",
        }
    
    response = client.post(
        url="/users/",
        json=data_dict
    )
    assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE
    



def test_get_user_by_id(client: TestClient, add_user):
    add_user(
        {
            "email": "test_user@test_domain.com",
            "username": "test_user",
            "password": "test_password",
        }
    )

    response = client.get(
        url="/users/1",
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["email"] == "test_user@test_domain.com"
