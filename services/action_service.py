from sqlalchemy.orm import Session

from models.data.action import Action
from models.request.action import ActionCreate
from repository.action_repository import ActionRepository


class ActionService:
    def __init__(self, db: Session):
        self.action_repository: ActionRepository = ActionRepository(db)

    def create_action(self, ticket_id: int, resource_id: int, action: ActionCreate):
        db_action: Action = Action(ticket_id=ticket_id, resource_id=resource_id, description=action.description)
        return self.action_repository.save(db_action=db_action)

    def get_actions(self):
        actions = self.action_repository.find_all()
        return actions
