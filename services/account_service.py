from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.request.account import AccountCreate
from repository.account_repository import AccountRepository


class AccountService:
    def __init__(self, db: Session):
        self.account_repository: AccountRepository = AccountRepository(db)

    def create_account(self, account: AccountCreate):
        if account.balance < 0:
            raise HTTPException(status_code=400, detail="Cannot create negative balance account")
        return self.account_repository.create_account(account=account)

    def get_accounts(self):
        return self.account_repository.find_all()
