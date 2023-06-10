from enum import Enum

from pydantic import BaseModel


class TransactionType(str, Enum):
    withdraw = "withdraw"
    deposit = "deposit"


class TransactionBase(BaseModel):
    amount: int
    type: TransactionType


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    cbu: int

    class Config:
        orm_mode = True
