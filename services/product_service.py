from repository.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository: ProductRepository = ProductRepository()

    def get_products(self):
        return self.product_repository.get_products()
