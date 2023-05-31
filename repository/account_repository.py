from sqlalchemy.orm import Session

from models.data.account import AccountDB
from models.request.account import AccountCreate


class AccountRepository:
    def __init__(self, sess: Session):
        self.db = sess

    def create_account(self, account: AccountCreate):
        db_account = AccountDB(balance=account.balance)
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account

    def find_all(self):
        return self.db.query(AccountDB).all()
