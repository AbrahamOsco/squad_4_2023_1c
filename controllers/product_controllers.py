from fastapi import APIRouter
from models.request.product import Product

router = APIRouter()

products = [
    Product(id=1, name="Siu Guarani", version="1.0"),
    Product(id=2, name="Siu Guarani", version="2.0"),
]


@router.get("/products", response_model=list[Product])
def get_products():
    return products
