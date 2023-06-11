from sqlalchemy.orm import Session

from models.data.product import Product
from models.request.product import ProductCreate
from repository.product_repository import ProductRepository


class ProductService:
    def __init__(self, db: Session):
        self.product_repository: ProductRepository = ProductRepository(db)

    def get_products(self):
        return self.product_repository.get_products()

    def create_product(self, product: ProductCreate):
        db_product: Product = Product(name=product.name, version=product.version)
        return self.product_repository.save(db_product=db_product)
