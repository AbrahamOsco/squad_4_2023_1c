from sqlalchemy.orm import Session

from repository.account_repository import AccountRepository


class AccountService:

    def __init__(self, db: Session):
        self.account_repository: AccountRepository = AccountRepository(db)

    def get_accounts(self, skip: int = 0, limit: int = 100):
        return self.account_repository.find_all(skip, limit)
