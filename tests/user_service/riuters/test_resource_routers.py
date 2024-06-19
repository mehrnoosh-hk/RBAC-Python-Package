from fastapi.testclient import TestClient


def test_create_new_resource(client: TestClient):
    response = client.post(
        "/resources/",
        json={"name": "Resource 1", "description": "A resource."},
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Resource 1"
    assert response.json()["description"] == "A resource."


def test_can_not_create_same_resource_twice(client: TestClient, add_resource):
    add_resource()
    response = client.post(
        "/resources",
        json={"name": "Resource 1", "description": "A resource."}
    )

    assert response.status_code == 406
    assert response.json() == {"error": "Resource already exists"}
