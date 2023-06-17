from sqlalchemy.orm import Session

from app.models.data.action import Action
from app.models.request.action import ActionCreate
from app.repository.action_repository import ActionRepository


class ActionService:
    def __init__(self, db: Session):
        self.action_repository: ActionRepository = ActionRepository(db)

    def create_action(self, ticket_id: int, resource_id: int, amount_hours: int , action: ActionCreate):
        db_action: Action = Action(ticket_id=ticket_id, resource_id=resource_id,
                                   amount_hours=amount_hours, time_start=action.time_start,
                                   time_end=action.time_end, description=action.description)
        return self.action_repository.save(db_action=db_action)

    def get_actions(self):
        actions = self.action_repository.find_all()
        return actions

    def get_actions_for_ticket(self, ticket_id: int):
        actions = self.action_repository.find_by_ticket(ticket_id=ticket_id)
        return actions
