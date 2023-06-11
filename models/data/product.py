from sqlalchemy import Column, Integer, String

from database.connection import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    version = Column(String)