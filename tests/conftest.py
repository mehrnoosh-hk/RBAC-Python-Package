import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from app.core.database import get_session
from app.main import password_manager


@pytest.fixture(scope="session")
def database_url():
    return "sqlite:///testing.db"


@pytest.fixture(scope="session")
def engine(database_url):
    return create_engine(database_url, echo=True, connect_args={"check_same_thread": False})


@pytest.fixture(scope="session", autouse=True)
def setup_database(engine, request):
    SQLModel.metadata.create_all(engine)

    def teardown():
        SQLModel.metadata.drop_all(engine)

    request.addfinalizer(teardown)


@pytest.fixture
def override_get_session(engine):
    def _override_get_session() -> Session:
        with Session(engine) as session:
            yield session

    return _override_get_session


@pytest.fixture
def client(override_get_session):
    password_manager.dependency_overrides[get_session] = override_get_session
    with TestClient(password_manager) as client:
        yield client


@pytest.fixture
def session():
    with Session(engine) as session:
        yield session
        session.rollback()
