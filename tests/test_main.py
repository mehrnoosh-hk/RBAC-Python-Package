from app.main import password_manager
from fastapi.testclient import TestClient


client = TestClient(password_manager)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
