from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    response = client.post(
        "/users/",
        json={"email": "test_user@test_domain.com", "username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 201
    assert response.json() == {"username": "test_user"}

    response = client.get("/users/")
    assert response.status_code == 200
    
    assert len(response.json()) == 1
    assert response.json()[0]["username"] == "test_user"
