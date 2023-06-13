from sqlalchemy.orm import Session

from models.data.ticket import Ticket


class TicketRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def save(self, db_ticket: Ticket):
        self.db.add(db_ticket)
        self.db.commit()
        self.db.refresh(db_ticket)
        return db_ticket

    def find_all(self):
        return self.db.query(Ticket).all()

    def delete(self, db_ticket: Ticket):
        self.db.delete(db_ticket)
        self.db.commit()
        return {"message": "Ticket deleted"}

    def find_by_id(self, ticket_id: int):
        return self.db.query(Ticket).get(ticket_id)

    def find_by_id_product(self, product_id: int):
        return self.db.query(Ticket).filter(Ticket.product_id == product_id).all()

