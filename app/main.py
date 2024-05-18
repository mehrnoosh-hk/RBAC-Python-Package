from fastapi import FastAPI


password_manager = FastAPI(
    title="Password Manager",
    description="A sophisticated password manager",
    version="0.1.0"
)


@password_manager.get("/")
async def root():
    return {"msg": "Hello World"}
