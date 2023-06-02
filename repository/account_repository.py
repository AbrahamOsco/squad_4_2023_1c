from sqlalchemy.orm import Session

from models.data.account import Account
from models.data.transaction import Transaction


class AccountRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def find_all(self):
        return self.db.query(Account).all()

    def save(self, db_account: Account):
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account

    def find_by_id(self, cbu: int):
        return self.db.query(Account).get(cbu)
