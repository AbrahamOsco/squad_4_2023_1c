from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.action import Action, ActionCreate
from services.action_service import ActionService

router = APIRouter()


@router.post("/action/ticket/{ticket_id}/resource/{resource_id}", response_model=Action)
def create_action(ticket_id: int, resource_id: int, action: ActionCreate, db: Session = Depends(get_db)):
    action_service: ActionService = ActionService(db)
    return action_service.create_action(ticket_id=ticket_id, resource_id=resource_id, action=action)


@router.get("/actions", response_model=list[Action])
def get_actions(db: Session = Depends(get_db)):
    action_service: ActionService = ActionService(db)
    return action_service.get_actions()
