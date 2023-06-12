from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.connection import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    type = Column(String)

    # Definimos una columna cbu de tipo Integer y hace
    # referencia a la columan cbu de la tabla accoutns.
    cbu = Column(Integer, ForeignKey("accounts.cbu"))

    # Establecemos una relacion  entre las tablas accounts y la tabla
    # transaccion  Account es el nombre de la clase relacionada.
    # y transactions es el atributo (variable) de relacion en la clase accoutns.
    owner = relationship("Account", back_populates="transactions")
