import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:qweasdzxc@localhost:5433/lottery" #os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"


settings = Settings()