from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.request.item import ItemCreate
from models.request.user import UserCreate
from repository.user import UserRepository


class UserService:

    def __init__(self, db: Session):
        self.repo: UserRepository = UserRepository(db)

    def create_user(self, user: UserCreate):
        db_user = self.repo.get_user_by_email(email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.repo.create_user(user=user)

    def get_users(self, skip: int = 0, limit: int = 100):
        user = self.repo.get_users(skip, limit)
        return user

    def get_user(self, user_id: int):
        db_user = self.repo.get_user(user_id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    def create_user_item(self, item: ItemCreate, user_id: int):
        return self.repo.create_user_item(item=item, user_id=user_id)

    def get_items(self, skip: int = 0, limit: int = 100):
        items = self.repo.get_items(skip=skip, limit=limit)
        return items
