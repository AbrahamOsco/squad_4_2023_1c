from sqlalchemy import Column, Integer, String

from database.connection import Base, SessionLocal


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    version = Column(String)


def initialize_db():
    db = SessionLocal()

    item1 = Product(name="Item 1", version="Description 1")
    item2 = Product(name="Item 2", version="Description 2")

    db.add(item1)
    db.add(item2)

    db.commit()
    db.close()