from enum import Enum

from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: int
    transaction_type: str


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    transaction_id: int
    owner_id: int

    class Config:
        orm_mode = True
