from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.connection import Base


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    resource_id = Column(Integer)
    description = Column(String)

    owner = relationship("Ticket", back_populates="actions")
