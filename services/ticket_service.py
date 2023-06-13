from fastapi import HTTPException
from requests import Session

from models.data.ticket import Ticket
from models.request.ticket import TicketCreate
from repository.ticket_repository import TicketRepository


class TicketService:
    def __init__(self, db: Session):
        self.ticket_repository: TicketRepository = TicketRepository(db)

    def create_ticket(self, product_id: int, client_id: int, ticket: TicketCreate):
        db_ticket: Ticket = Ticket(product_id=product_id, client_id=client_id, title=ticket.title,
                                   description=ticket.description, severity=ticket.severity,
                                   priority=ticket.priority, state=ticket.state,
                                   timeStart=ticket.timeStart, supportLevel=ticket.supportLevel,
                                   accumulatedTime=ticket.accumulatedTime)
        return self.ticket_repository.save(db_ticket=db_ticket)

    def get_tickets(self):
        return self.ticket_repository.find_all()

    def get_tickets_by_product_id(self, product_id: int):
        db_ticket: Ticket = self.ticket_repository.find_by_id_product(product_id=product_id)
        if db_ticket is None or len(list(db_ticket)) == 0: ## si la lista es nula entonces devolvemos tickets no found.
            raise HTTPException(status_code=404, detail="ticket associated with product id not found")
        return db_ticket

    def delete_ticket(self, ticket_id: int):
        db_ticket: Ticket = self.ticket_repository.find_by_id(ticket_id=ticket_id)
        if db_ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return self.ticket_repository.delete(db_ticket)

    def update_ticket(self, ticket_id: int, ticket: TicketCreate):
        db_ticket: Ticket = self.ticket_repository.find_by_id(ticket_id=ticket_id)
        if db_ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        db_ticket.title = ticket.title
        db_ticket.description = ticket.description
        db_ticket.severity = ticket.severity
        db_ticket.priority = ticket.priority
        db_ticket.state = ticket.state
        db_ticket.timeStart = ticket.timeStart
        db_ticket.supportLevel = ticket.supportLevel
        db_ticket.accumulatedTime = ticket.accumulatedTime
        return self.ticket_repository.save(db_ticket=db_ticket)
