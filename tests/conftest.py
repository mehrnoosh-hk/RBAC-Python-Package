from typing import Callable

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from app.core.database import Base, get_session
from main import resource_manager


@pytest.fixture(scope="session")
def database_url() -> str:
    return "sqlite:///testing.db"


@pytest.fixture(scope="session")
def engine(database_url: str) -> Engine:
    return create_engine(
        database_url, echo=True, connect_args={"check_same_thread": False}
    )


@pytest.fixture(scope="function", autouse=True)
def setup_database(engine: Engine, request) -> None:
    Base.metadata.create_all(engine)

    def teardown() -> None:
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)


@pytest.fixture
def override_get_session(engine: Engine) -> Callable:
    def _override_get_session():
        with Session(engine) as session:
            yield session

    return _override_get_session


@pytest.fixture
def client(override_get_session):
    resource_manager.dependency_overrides[get_session] = override_get_session
    with TestClient(resource_manager) as client:
        yield client


@pytest.fixture
def add_user(client: TestClient) -> Callable:
    def _add_user(user_data: dict):
        client.post("/users/", json=user_data)

    return _add_user


@pytest.fixture
def add_role(client: TestClient) -> Callable:
    role_data = {"name": "admin", "description": "admin role"}

    def _add_role():
        client.post("/roles/", json=role_data)

    return _add_role


@pytest.fixture
def add_roles(client: TestClient) -> Callable:
    def _add_roles():
        roles = [
            {"name": "admin", "description": "admin role"},
            {"name": "user", "description": "user role"},
            {"name": "guest", "description": "guest role"},
        ]
        for role in roles:
            client.post("/roles/", json=role)

    return _add_roles


@pytest.fixture
def add_resource(client: TestClient) -> Callable:
    def _add_resource() -> None:
        resource = {"name": "Resource test 1", "description": "A resource."}
        client.post("/resources/", json=resource)
    
    return _add_resource


@pytest.fixture
def add_resources(client: TestClient) -> Callable:
    def _add_resource():
        resources = [
            {"name": "Resource 1", "description": "A resource."},
            {"name": "Resource 2", "description": "Another resource."},
            {"name": "Resource 3", "description": "Yet another resource."},
        ]
        for resource in resources:
            client.post("/resources/", json=resource)

    return _add_resource


@pytest.fixture
def add_permission(client: TestClient) -> Callable:
    def _add_permission():
        permission = {
            "name": "Permission to duplicate",
            "description": "A permission"
        }
        client.post(
            url="/permissions",
            json=permission
        )
    return _add_permission