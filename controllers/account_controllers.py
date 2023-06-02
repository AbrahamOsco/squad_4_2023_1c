from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.account import Account
from services.account_service import AccountService

router = APIRouter()


@router.get("/accounts", response_model=list[Account])
def get_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    account_service: AccountService = AccountService(db)
    return account_service.get_accounts(skip=skip, limit=limit)
