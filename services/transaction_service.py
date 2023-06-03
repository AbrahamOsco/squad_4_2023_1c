from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.data.transaction import Transaction
from repository.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, db: Session):
        self.transaction_repository: TransactionRepository = TransactionRepository(db)

    def get_transactions(self):
        transactions = self.transaction_repository.find_all()
        return transactions

    def find_by_id(self, transaction_id: int):
        db_transaction: Transaction = self.transaction_repository.find_by_id(transaction_id=transaction_id)
        if db_transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return db_transaction

    def find_by_cbu(self, cbu: int):
        transactions = self.transaction_repository.find_by_cbu(cbu=cbu)
        return transactions
