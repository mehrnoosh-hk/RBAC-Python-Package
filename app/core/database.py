from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "postgresql://your_user:your_password@localhost/your_db"


engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


def get_session():
    with Session(engine) as session:
        yield session
