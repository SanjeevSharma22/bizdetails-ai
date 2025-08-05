from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost:5432/bizdetails"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "CHANGE_ME"

    class Config:
        env_file = ".env"


settings = Settings()
