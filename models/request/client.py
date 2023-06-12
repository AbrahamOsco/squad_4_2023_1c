from pydantic import BaseModel


class ClientBase(BaseModel):
    razon_social: str
    cuit: str


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
