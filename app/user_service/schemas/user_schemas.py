import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str
    enabled: bool = True


class User(UserBase):
    id: int
    enabled: bool | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    deleted: bool | None
    deleted_at: datetime.datetime | None

    class Config:
        from_attributes = True
