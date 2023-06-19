from fastapi import APIRouter, Depends
from requests import Session

from app.database.connection import get_db
from app.models.request.ticket import Ticket, TicketCreate, TicketUpdateSupport, TicketUpdateTime
from app.services.ticket_service import TicketService

router = APIRouter()


@router.post("/ticket/product/{product_id}/client/{client_id}/responsible/{responsible_id}", response_model=Ticket)
def create_ticket(product_id: int, client_id: int, responsible_id: int,
                  ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket_service: TicketService = TicketService(db)
    return ticket_service.create_ticket(product_id=product_id, client_id=client_id,
                                        responsible_id=responsible_id, ticket=ticket)


@router.get("/tickets", response_model=list[Ticket])
def get_tickets(db: Session = Depends(get_db)):
    ticket_service: TicketService = TicketService(db)
    return ticket_service.get_tickets()


@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket_service: TicketService = TicketService(db)
    return ticket_service.delete_ticket(ticket_id=ticket_id)


@router.put("/tickets/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket_service: TicketService = TicketService(db)
    return ticket_service.update_ticket(ticket_id=ticket_id, ticket=ticket)


@router.get("/tickets/{product_id}", response_model=list[Ticket])
def get_tickets(product_id: int, db: Session = Depends(get_db)):
    ticket_service: TicketService = TicketService(db)
    return ticket_service.get_tickets_by_product_id(product_id)
