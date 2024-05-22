import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

from app.core.database import get_session
from app.main import password_manager


DATABASE_URL = "sqlite:///testing.db"
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


def override_get_session() -> Session:
    with Session(engine) as session:
        yield session


password_manager.dependency_overrides[get_session] = override_get_session


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def client():
    return TestClient(password_manager)


@pytest.fixture
def session():
    with Session(engine) as session:
        yield session
        session.rollback()
