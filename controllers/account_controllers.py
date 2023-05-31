from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.account import Account
from services.account_service import AccountService

router = APIRouter()


@router.post("/accounts", response_model=Account)
def create_account(account: Account, db: Session = Depends(get_db)):
    account_service: AccountService = AccountService(db)
    return account_service.create_account(account)
