from sqlalchemy import Column, Integer, String

from database.connection import Base, SessionLocal


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    version = Column(String)


def initialize_db():
    db = SessionLocal()

    item1 = Product(name="Siu Guarani", version="versio 1.0")
    item2 = Product(name="Siu Guarani", version="version 1.1")

    db.add(item1)
    db.add(item2)

    db.commit()
    db.close()