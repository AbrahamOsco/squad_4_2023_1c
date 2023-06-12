from fastapi import APIRouter, Depends
from requests import Session

from database.connection import get_db
from models.request.ticket import Ticket, TicketCreate
from services.ticket_service import TicketService

router = APIRouter()


@router.post("/product/{product_id}/client/{client_id}", response_model=Ticket)
def create_ticket(product_id: int, client_id, ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket_service: TicketService = TicketService(db)
    return ticket_service.create_ticket(product_id=product_id, client_id=client_id, ticket=ticket)
