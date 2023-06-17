from pydantic import BaseModel


class ActionBase(BaseModel):
    description: str
    time_start: str
    time_end: str


class ActionCreate(ActionBase):
    pass


class Action(ActionBase):
    id: int
    ticket_id: int
    resource_id: int
    amount_hours: int

    class Config:
        orm_mode = True
