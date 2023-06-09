from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    client_id = Column(Integer)

    responsible_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    severity = Column(String)
    priority = Column(String)
    state = Column(String)
    timeStart = Column(String)
    type = Column(String)
    supportTime = Column(Integer)

    assignments = relationship("Assignment", back_populates="owner")




