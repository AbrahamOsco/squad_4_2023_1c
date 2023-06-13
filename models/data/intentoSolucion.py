
from sqlalchemy import Column, String, Integer

from database.connection import Base


class IntentoDeSolucion(Base):
    __tablename__ = "intentoDeSolucion"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)


