from pydantic import BaseModel

from models.request.action import Action


class TicketBase(BaseModel):
    current_responsible_id: int
    title: str
    description: str
    severity: str
    priority: str
    state: str
    timeStart: str
    supportLevel: str
    accumulatedTime: str


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    product_id: int
    client_id: int
    actions: list[Action] = []

    class Config:
        orm_mode = True
