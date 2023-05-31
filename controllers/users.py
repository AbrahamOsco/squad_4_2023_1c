from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.item import Item, ItemCreate
from models.request.user import UserCreate, User
from services.user import UserService

router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service: UserService = UserService(db)
    return user_service.create_user(user=user)


@router.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_service: UserService = UserService(db)
    return user_service.get_users(skip=skip, limit=limit)


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service: UserService = UserService(db)
    return user_service.get_user(user_id=user_id)


@router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
        user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    user_service: UserService = UserService(db)
    return user_service.create_user_item(item=item, user_id=user_id)
