from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.product import Product, ProductCreate
from services.product_service import ProductService

router = APIRouter()


@router.post("/products", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_service: ProductService = ProductService(db)
    return product_service.create_product(product=product)


@router.get("/products", response_model=list[Product])
def get_products(db: Session = Depends(get_db)):
    product_service: ProductService = ProductService(db)
    return product_service.get_products()
