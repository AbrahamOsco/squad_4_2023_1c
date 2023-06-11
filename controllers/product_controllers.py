from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.product import Product
from services.product_service import ProductService

router = APIRouter()


@router.get("/products", response_model=list[Product])
def get_accounts(db: Session = Depends(get_db)):
    product_service: ProductService = ProductService(db)
    return product_service.get_products()
