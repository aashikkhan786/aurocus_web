"""Application configuration using Pydantic BaseSettings."""

import secrets
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    model_config = SettingsConfigDict(env_file=".env")

    SITE_URL: str = "http://localhost:8000"
    SITE_NAME: str = "Aurocous"
    DATABASE_URL: str = "aurocous.db"
    SECRET_KEY: str = secrets.token_hex(32)
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "admin123"


settings = Settings()
