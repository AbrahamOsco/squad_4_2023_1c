from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.data.account import Account
from models.request.account import AccountCreate
from repository.account_repository import AccountRepository


class AccountService:

    def __init__(self, db: Session):
        self.account_repository: AccountRepository = AccountRepository(db)

    def get_accounts(self, skip: int = 0, limit: int = 100):
        return self.account_repository.find_all(skip, limit)

    def create_account(self, account: AccountCreate):
        if account.balance < 0:
            raise HTTPException(status_code=400, detail="Cannot create negative balance account")
        db_account = Account(balance=account.balance)
        return self.account_repository.save(db_account=db_account)
