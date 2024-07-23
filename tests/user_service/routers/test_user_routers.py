from fastapi import status
from fastapi.testclient import TestClient
from app.user_service.models.user_crud import get_user_by_id
from app.auth_service.security import verify_password


def test_create_user(client: TestClient):
    data_dict = {
        "email": "test_user@test_domain.com",
        "username": "test_user",
        "password": "test_password",
        "enabled": True,
    }
    response = client.post(url="/users/", json=data_dict)
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

    response = client.post(url="/users/", json=data_dict)
    assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE


def test_password_is_not_saved_as_plain_text(client: TestClient, add_user, override_get_session):
    add_user({
            "email": "test_user@test_domain.com",
            "username": "test_user",
            "password": "test_password",
        })
    
    session_generator = override_get_session()
    session = next(session_generator)

    user = get_user_by_id(session, 1)

    assert user
    assert user.email == "test_user@test_domain.com"
    assert user.password != "test_password"
    assert verify_password("test_password", user.password) is True


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
