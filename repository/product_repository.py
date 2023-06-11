from sqlalchemy.orm import Session

from models.data.product import Product


class ProductRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def get_products(self):
        return self.db.query(Product).all()

    def save(self, db_product: Product):
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

