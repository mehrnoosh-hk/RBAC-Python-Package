from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///db.sqlite"
    pythonpath: str = "/app"

    class Config:
        env_file = ".env"


settings = Settings()
