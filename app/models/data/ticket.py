from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    project_id = Column(Integer, nullable=True)
    client_id = Column(Integer)

    responsible_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    severity = Column(String)
    priority = Column(String)
    state = Column(String)
    timeStart = Column(String)
    type = Column(String)
    supportTime = Column(String)






