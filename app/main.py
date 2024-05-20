from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.user_service.routers.user_router import user_router
from app.core.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


password_manager = FastAPI(
    title="Password Manager",
    description="A sophisticated password manager",
    version="0.1.0",
    lifespan=lifespan
)

password_manager.include_router(user_router)


@password_manager.get("/")
async def root():
    return {"msg": "Hello World"}
