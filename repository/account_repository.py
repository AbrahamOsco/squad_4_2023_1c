from sqlalchemy.orm import Session

from models.data.account import Account
from models.data.transaction import Transaction


class AccountRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def find_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Account).offset(skip).limit(limit).all()
