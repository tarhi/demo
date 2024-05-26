from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.users import UserCreateSchemas, UserUpdateSchemas
from app.services.credentials import verify_password


class CRUDUsers(CRUDBase(UserCreateSchemas, UserUpdateSchemas)):
    def login(self, db: Session, *, email: str , password:str) -> User: 
        user = db.query(self).filter(User.email== email).first()
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user
    

UsersCrud= CRUDUsers(User)


