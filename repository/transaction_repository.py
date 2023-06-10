from sqlalchemy.orm import Session

from models.data.transaction import Transaction


class TransactionRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def find_all(self):
        return self.db.query(Transaction).all()

    def find_by_id(self, transaction_id: int):
        return self.db.query(Transaction).get(transaction_id)

    def find_by_cbu(self, cbu: int):
        return self.db.query(Transaction).filter_by(cbu=cbu).all()
