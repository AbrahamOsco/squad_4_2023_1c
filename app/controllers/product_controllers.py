from fastapi import APIRouter
from app.models.request.product import Product

router = APIRouter()

products = [
    Product(id=1, name="Siu Guarani", version="1.0.0"),
    Product(id=2, name="Siu Guarani", version="2.0.0"),
    Product(id=3, name="Gestion de Inventario", version="1.0.0"),
    Product(id=4, name="Sistema de Tickets", version="1.0.0"),
    Product(id=5, name="Sistema de Molinetes", version="1.0.0")
]


@router.get("/products", response_model=list[Product])
def get_products():
    return products


@router.get("/product/{id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}
