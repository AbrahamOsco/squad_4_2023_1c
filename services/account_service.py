from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.data.account import Account
from models.data.transaction import Transaction
from models.request.account import AccountCreate
from models.request.transaction import TransactionCreate, TransactionType
from repository.account_repository import AccountRepository


class AccountService:

    def __init__(self, db: Session):
        self.account_repository: AccountRepository = AccountRepository(db)

    def create_account(self, account: AccountCreate):
        if account.balance < 0:
            raise HTTPException(status_code=400, detail="Cannot create negative balance account")
        db_account: Account = Account(balance=account.balance)
        return self.account_repository.save_account(db_account=db_account)

    def get_accounts(self):
        account = self.account_repository.find_all()
        return account

    def find_by_id(self, cbu: int):
        db_account: Account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_account

    def update_account(self, cbu: int, account: AccountCreate):
        db_account: Account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        if account.balance < 0:
            raise HTTPException(status_code=400, detail="Cannot update account with negative balance")
        db_account.balance = account.balance
        return self.account_repository.save_account(db_account=db_account)

    def create_account_transaction(self, transaction: TransactionCreate, cbu: int):
        if transaction.type == TransactionType.withdraw:
            self.withdraw(cbu, transaction.amount)
        elif transaction.type == TransactionType.deposit:
            self.deposit(cbu, transaction.amount)
        else:
            raise HTTPException(status_code=400, detail="Invalid transaction type")
        db_transaction: Transaction = Transaction(amount=transaction.amount, type=transaction.type, cbu=cbu)
        return self.account_repository.save_transaction(db_transaction=db_transaction)

    def withdraw(self, cbu: int, amount: int):
        db_account: Account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        if amount == 0:
            raise HTTPException(status_code=400, detail="Cannot withdraw null amounts")
        if amount < 0:
            raise HTTPException(status_code=400, detail="Cannot withdraw negative amounts")
        if db_account.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        db_account.balance = db_account.balance - amount
        self.account_repository.save_account(db_account)

    def deposit(self, cbu: int, amount: int):
        if amount == 0:
            raise HTTPException(status_code=400, detail="Cannot deposit null amounts")
        if amount < 0:
            raise HTTPException(status_code=400, detail="Cannot deposit negative amounts")
        if amount >= 2000:
            extra = min(amount * 0.1, 500)
            amount += extra
        db_account: Account = self.account_repository.find_by_id(cbu=cbu)
        if db_account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        db_account.balance = db_account.balance + amount
        self.account_repository.save_account(db_account)
