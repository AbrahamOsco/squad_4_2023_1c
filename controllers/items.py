from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.item import Item
from services.user import UserService

router = APIRouter()


@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_service: UserService = UserService(db)
    return user_service.get_items(skip=skip, limit=limit)
