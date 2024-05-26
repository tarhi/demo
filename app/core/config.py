import secrets
from typing import Any, Optional
from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv(encoding="utf-8")


class Settings(BaseSettings):
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT")
    API_VERSION: str = os.environ.get("API_VERSION")
    PROJECT_NAME: str = os.environ.get("PROJECT_NAME")
    # FILE_VOLUME: str = os.environ.get("FILE_VOLUME")
    # TEMPLATES_DIR: str
    # EMAIL_TEMPLATES_DIR: str
    # SECRET_KEY: str = os.environ.get("SECRET_KEY")
    SECRET_KEY: str = secrets.token_hex(32)
    ALGORITHM: str = os.environ.get("ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES")
    EMAIL_RESET_TOKEN_EXPIRE_MINUTES: int = os.environ.get(
        "EMAIL_RESET_TOKEN_EXPIRE_MINUTES"
    )
    TOKEN_TYPE: str = os.environ.get("TOKEN_TYPE")

    # The `POSTGRES_USER` variable is being used to store the value of the PostgreSQL username. It is
    # retrieving the value from the environment variables using `os.environ.get("")`.
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOSTNAME: str = os.environ.get("POSTGRES_HOSTNAME")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")

    SQLALCHEMY_DATABASE_URI: Optional[Any] = None

    @field_validator("SQLALCHEMY_DATABASE_URI")
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        """Validate db url settings."""
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOSTNAME"),
            port=values.data.get("POSTGRES_PORT"),
            path=values.data.get("POSTGRES_DB"),
        )


settings = Settings()
