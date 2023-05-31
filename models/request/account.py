from pydantic import BaseModel


class Account(BaseModel):
    cbu: int
    balance: int

    class Config:
        orm_mode = True
