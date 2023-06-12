from requests import Session

from models.data.ticket import Ticket
from models.request.ticket import TicketCreate
from repository.ticket_repository import TicketRepository


class TicketService:
    def __init__(self, db: Session):
        self.product_repository: TicketRepository = TicketRepository(db)

    def create_ticket(self, product_id: int, client_id: int, ticket: TicketCreate):
        db_ticket: Ticket = Ticket(product_id=product_id, client_id=client_id, title=ticket.title)
        return self.product_repository.save(db_ticket=db_ticket)
