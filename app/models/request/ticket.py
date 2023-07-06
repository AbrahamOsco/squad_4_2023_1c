from typing import Optional

from pydantic import BaseModel

from app.models.request.assignment import Assignment


class TicketBase(BaseModel):
    title: str
    description: str
    severity: str
    priority: str
    state: str
    timeStart: str
    type: str
    supportTime: int


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    product_id: int
    client_id: int
    responsible_id: int

    class Config:
        orm_mode = True
