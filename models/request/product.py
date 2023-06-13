from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    version: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orn_mode = True
