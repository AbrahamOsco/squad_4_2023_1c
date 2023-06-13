from sqlalchemy import Column, Integer, String

from database.connection import Base


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer)
    resource_id = Column(Integer)
    description = Column(String)
