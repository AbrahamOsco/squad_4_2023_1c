from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from database.connection import Base


# Se crea la clase Account que ehera de base esto representa
# una tabla llamada account en la base de datos.
class Account(Base):
    __tablename__ = "accounts"  # especifica el nombre de la tabla de la base de datos.

    cbu = Column(Integer, primary_key=True, index=True)  # Define una columna en la tabla accounts cuyo tipo es un
    # Inteneger y es la primary key y tiene indice.
    balance = Column(Integer)  # Define una columan en la tabla accounts cuyo tipo es un integer.

    transactions = relationship("Transaction", back_populates="owner")
    # Define una relacion entre la tabla accounts y la tabla transactions se basa en el atributo owner
    # de transactions. Relationship establece una relacion uno a muchos donde una cuenta puede tener
    # multiples transacciones. El atributo owner especifica el atributo de relacion en la clase
    # transacciones que apunta a una cuenta.

