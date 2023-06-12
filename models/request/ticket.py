from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    product_id: int
    client_id: int

    class Config:
        orm_mode = True