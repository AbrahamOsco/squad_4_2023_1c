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

    def find_by_id(self, cbu: int):
        db_account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_account

    def update_account(self, cbu: int, account: AccountCreate):
        db_account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        if account.balance < 0:
            raise HTTPException(status_code=400, detail="Cannot update account with negative balance")
        db_account.balance = account.balance
        return self.account_repository.save(db_account)

    def delete_by_id(self, cbu: int):
        db_account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        return self.account_repository.delete_by_id(db_account)
