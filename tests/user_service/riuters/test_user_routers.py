from fastapi.testclient import TestClient
from app.main import password_manager

client = TestClient(password_manager)


def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "test_user@test_domain.com", "username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 201
    assert response.json() == {"username": "test_user"}
