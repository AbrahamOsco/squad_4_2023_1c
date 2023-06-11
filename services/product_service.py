from sqlalchemy.orm import Session

from repository.product_repository import ProductRepository


class ProductService:
    def __init__(self, db: Session):
        self.product_repository: ProductRepository = ProductRepository(db)

    def get_products(self):
        return self.product_repository.get_products()
