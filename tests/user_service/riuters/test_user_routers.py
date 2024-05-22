from fastapi.testclient import TestClient
from sqlmodel import Session


def test_create_user(client: TestClient, session: Session):
    response = client.post(
        "/users/",
        json={"email": "test_user@test_domain.com", "username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 201
    assert response.json() == {"username": "test_user"}

    # check user created in database
    from app.user_service.models.user_crud import get_all_users
    users = get_all_users(session)
    assert len(users) == 1
    assert users[0].username == "test_user"
