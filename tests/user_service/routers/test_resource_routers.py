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
    add_resource({"name": "Resource test 1", "description": "A resource."})
    response = client.post(
        "/resources",
        json={"name": "Resource test 1", "description": "A resource."}
    )

    assert response.status_code == 406
    assert response.json() == {"error": "Resource already exists"}


def test_get_all_resources(client: TestClient, add_resources):
    add_resources(
        [
            {"name": "Resource 1", "description": "A resource."},
            {"name": "Resource 2", "description": "Another resource."},
            {"name": "Resource 3", "description": "Yet another resource."},
        ]
    )

    response = client.get(url="/resources")

    assert response.status_code == 200
    assert len(response.json()) == 3
