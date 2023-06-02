from sqlalchemy.orm import Session

from repository.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, db: Session):
        self.transaction_repository: TransactionRepository = TransactionRepository(db)

    def get_transactions(self):
        transactions = self.transaction_repository.find_all()
        return transactions
