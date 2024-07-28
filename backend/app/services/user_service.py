from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import UserCreate

class UserService:
    def create_user(self, db: Session, user: UserCreate):
        db_user = User(email=user.email, hashed_password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
