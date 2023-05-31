from sqlalchemy import Column, Integer

from database.connection import Base


class AccountDB(Base):
    __tablename__ = "accounts"

    cbu = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer, index=True)