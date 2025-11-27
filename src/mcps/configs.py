import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    ENV: str = Field(default="local")
    # Development mode flag
    model_config = SettingsConfigDict(
        env_file=os.getenv("ENVPATH") if os.getenv("ENVPATH") else ".env",
        extra="allow",
    )
    LOGS_DIR: str = Field(default="./logs")


settings = Settings()

try:
    os.makedirs(settings.LOGS_DIR, exist_ok=True)
except Exception as e:
    pass
