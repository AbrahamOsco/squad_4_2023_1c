from sqlalchemy.orm import Session

from models.data.product import Product


class ProductRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def get_products(self):
        return self.db.query(Product).all()

