from pydantic import BaseModel


class ActionBase(BaseModel):
    description: str


class ActionCreate(ActionBase):
    pass


class Action(ActionBase):
    id: int
    ticket_id: int
    resource_id: int

    class Config:
        orm_mode = True
