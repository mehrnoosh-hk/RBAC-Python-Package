from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.user_service.routers.user_router import user_router


resource_manager = FastAPI(
    title="Resource Management and Sharing System",
    description="A sophisticated system for managing and sharing resources.",
    version="0.1.0",
)

resource_manager.include_router(user_router)


@resource_manager.get("/")
async def root():
    return {"msg": "Hello World"}
