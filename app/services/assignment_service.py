from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.data.assignment import Assignment
from app.models.request.assignment import AssignmentCreate
from app.repository.assignment_repository import AssignmentRepository


class AssignmentService:
    def __init__(self, db: Session):
        self.assignment_repository: AssignmentRepository = AssignmentRepository(db)

    def create_assignment(self, ticket_id: int, assignment: AssignmentCreate):
        db_assignment: Assignment = Assignment(ticket_id=ticket_id, task_id=assignment.task_id,
                                               project_id=assignment.project_id)
        return self.assignment_repository.save(db_assignment=db_assignment)

    def get_assignments(self):
        assignments = self.assignment_repository.find_all()
        return assignments

    def get_assignments_by_ticket_id(self, ticket_id: int):
        assignments = self.assignment_repository.find_by_ticket(ticket_id=ticket_id)
        return assignments

    def get_assignments_by_task_id(self, task_id):
        assignments = self.assignment_repository.find_by_task(task_id=task_id)
        return assignments

    def delete_assignment(self, assignment_id: int):
        db_assignment: Assignment = self.assignment_repository.find_by_id(assignment_id=assignment_id)
        if db_assignment is None:
            raise HTTPException(status_code=404, detail="Assignment not found")
        return self.assignment_repository.delete(db_assignment)
