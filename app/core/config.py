from typing import Any, Optional
from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv(encoding="utf-8")


class Settings(BaseSettings):

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
