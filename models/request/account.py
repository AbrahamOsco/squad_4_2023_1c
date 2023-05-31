from pydantic import BaseModel


class AccountCreate(BaseModel):
    balance: int


class Account(AccountCreate):
    cbu: int

    class Config:
        orm_mode = True
