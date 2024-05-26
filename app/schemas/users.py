
# pour validatiobn des données venient du frontend 

from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr= None
    full_name: Optional[str] = None
    username: Optional[str]
    password: Optional[str] = Field(None, description="userpassword", example= "*****")
    

class UserCreateSchemas(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, description="userpassword", example= "*****")
    
    
class UserUpdateSchemas(UserBase):
    pass
    