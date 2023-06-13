from sqlalchemy import Column, Integer, String

from database.connection import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    client_id = Column(Integer)
    #attributes
    title = Column(String)
    description = Column(String)
    severity = Column(String)
    priority = Column(String)
    state = Column(String)
    timeStart = Column(String)
    supportLevel = Column(String)
    accumulatedTime = Column(String)







