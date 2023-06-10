from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.connection import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    type = Column(String)
    cbu = Column(Integer, ForeignKey("accounts.cbu"))

    owner = relationship("Account", back_populates="transactions")
