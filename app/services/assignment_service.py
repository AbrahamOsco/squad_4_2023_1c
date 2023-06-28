from sqlalchemy.orm import Session

from app.models.data.assignment import Assignment
from app.models.request.assignment import AssignmentCreate
from app.repository.assignment_repository import AssignmentRepository


class AssignmentService:
    def __init__(self, db: Session):
        self.assignment_repository: AssignmentRepository = AssignmentRepository(db)

    def create_assignment(self, ticket_id: int, assignment: AssignmentCreate):
        db_assignment: Assignment = Assignment(ticket_id=ticket_id, task_id=assignment.task_id)
        return self.assignment_repository.save(db_assignment=db_assignment)
