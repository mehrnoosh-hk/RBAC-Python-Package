from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = "postgresql://your_user:your_password@localhost/your_db"


engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)