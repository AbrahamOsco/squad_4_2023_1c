from sqlalchemy.orm import Session

from models.data.transaction import Transaction


class TransactionRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def find_all(self):
        return self.db.query(Transaction).all()
