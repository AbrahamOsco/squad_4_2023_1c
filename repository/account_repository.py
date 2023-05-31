from sqlalchemy.orm import Session

from models.data.account import AccountDB
from models.request.account import Account


class AccountRepository:
    def __init__(self, sess: Session):
        self.db = sess

    def create_account(self, account: Account):
        db_account = AccountDB(cbu=account.cbu, balance=account.balance)
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account
