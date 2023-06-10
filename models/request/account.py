from pydantic import BaseModel

from models.request.transaction import Transaction


class AccountBase(BaseModel):
    balance: int


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    cbu: int
    transactions: list[Transaction] = []

    class Config:
        orm_mode = True
        