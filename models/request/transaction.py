from enum import Enum

from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: int
    type: str


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    cbu: int

    class Config:
        orm_mode = True
