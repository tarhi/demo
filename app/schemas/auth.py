from typing import Optional

from pydantic import BaseModel, Field
from pydantic import BaseModel, EmailStr, Field


class TokenBase(BaseModel):
    access_token: Optional[str] = Field(...)
    refresh_token: Optional[str] = Field(...)


class TokenData(BaseModel):
    sub: Optional[str] = Field(...)
    exp: Optional[int] = Field(...)


class RefreshToken(BaseModel):
    refresh_token: Optional[str] = Field(...)


class UserCredentials(BaseModel):
    email: EmailStr = Field(
        ...,
        description="The email address of the user (unique | Email format).",
        example="user@example.com",
    )
    password: str = Field(
        ..., description="The password for the user.", example="string"
    )