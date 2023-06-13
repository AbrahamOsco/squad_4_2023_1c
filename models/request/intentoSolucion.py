from pydantic import BaseModel


class IntentoDeSolucionBase(BaseModel):
    descripcion: str


class IntentoDeSolucionCreate(IntentoDeSolucionBase):
    pass


class IntentoDeSolucion(IntentoDeSolucionBase):
    id: int

    class Config:
        orm_mode = True
