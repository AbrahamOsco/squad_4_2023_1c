from pydantic import BaseModel

from models.request.transaction import Transaction


class AccountBase(BaseModel):
    balance: int


class AccountCreate(AccountBase):
    pass


class Account(AccountCreate):
    cbu: int
    transactions: list[Transaction] = []

    class Config:
        orm_mode = True
