from fastapi import HTTPException
from requests import Session

from app.models.data.ticket import Ticket
from app.models.request.ticket import TicketCreate
from app.repository.ticket_repository import TicketRepository


class TicketService:
    def __init__(self, db: Session):
        self.ticket_repository: TicketRepository = TicketRepository(db)

    def create_ticket(self, product_id: int, client_id: int, responsible_id: int, ticket: TicketCreate):
        ticket_data = ticket.dict()
        ticket_data.update({
            "product_id": product_id,
            "client_id": client_id,
            "responsible_id": responsible_id,
            "project_id": None
        })
        db_ticket = Ticket(**ticket_data)
        return self.ticket_repository.save(db_ticket=db_ticket)

    def get_tickets(self):
        return self.ticket_repository.find_all()

    def get_tickets_by_product_id(self, product_id: int):
        db_ticket: Ticket = self.ticket_repository.find_by_id_product(product_id=product_id)
        if db_ticket is None or len(list(db_ticket)) == 0:
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
        db_ticket.type = ticket.type
        db_ticket.supportTime = ticket.supportTime
        db_ticket.project_id = ticket.project_id
        return self.ticket_repository.save(db_ticket=db_ticket)

    def get_ticket(self, ticket_id: int):
        db_ticket: Ticket = self.ticket_repository.find_by_id(ticket_id=ticket_id)
        if db_ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return db_ticket

    def get_tickets_by_project_id(self, project_id: int):
        db_ticket: Ticket = self.ticket_repository.find_by_id_project(project_id=project_id)
        if db_ticket is None or len(list(db_ticket)) == 0:
            raise HTTPException(status_code=404, detail="ticket associated with project id not found")
        return db_ticket
