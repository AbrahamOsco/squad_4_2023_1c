from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.account import Account, AccountCreate
from services.account_service import AccountService

router = APIRouter()


@router.post("/accounts", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    account_service: AccountService = AccountService(db)
    return account_service.create_account(account=account)


@router.get("/accounts", response_model=list[Account])
def get_accounts(db: Session = Depends(get_db)):
    account_service: AccountService = AccountService(db)
    return account_service.get_accounts()
