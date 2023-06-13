from requests import Session

from models.data.ticket import Ticket
from models.request.ticket import TicketCreate
from repository.ticket_repository import TicketRepository


class TicketService:
    def __init__(self, db: Session):
        self.ticket_repository: TicketRepository = TicketRepository(db)

    def create_ticket(self, product_id: int, client_id: int, ticket: TicketCreate):
        db_ticket: Ticket = Ticket(product_id=product_id, client_id=client_id, title=ticket.title)
        return self.ticket_repository.save(db_ticket=db_ticket)

    def get_tickets(self):
        tickets = self.ticket_repository.find_all()
        return tickets

    def delete_ticket(self, ticket_id: int):
        return self.ticket_repository.delete(ticket_id)
