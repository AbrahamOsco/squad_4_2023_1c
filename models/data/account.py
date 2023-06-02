from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from database.connection import Base


class Account(Base):
    __tablename__ = "accounts"

    cbu = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer)

    transactions = relationship("Transaction", back_populates="owner")
