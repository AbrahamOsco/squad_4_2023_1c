from typing import Optional

from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    description: str
    severity: str
    priority: str
    state: str
    timeStart: str
    type: str
    supportTime: str
    project_id: Optional[int]


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    product_id: int
    client_id: int
    responsible_id: int

    class Config:
        orm_mode = True
