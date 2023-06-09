from fastapi import APIRouter

from models.request.product import Product
from services.product_service import ProductService

router = APIRouter()


@router.get("/products", response_model=list[Product])
def get_accounts():
    product_service: ProductService = ProductService()
    return product_service.get_products()
