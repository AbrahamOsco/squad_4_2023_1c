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
