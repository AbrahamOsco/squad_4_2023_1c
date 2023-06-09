from fastapi import APIRouter, Depends
from requests import Session

from app.database.connection import get_db
from app.models.request.assignment import Assignment, AssignmentCreate
from app.services.assignment_service import AssignmentService

router = APIRouter()


@router.post("/assignments/ticket/{ticket_id}", response_model=Assignment)
def create_assignment(ticket_id: int, assignment: AssignmentCreate, db: Session = Depends(get_db)):
    assignment_service: AssignmentService = AssignmentService(db)
    return assignment_service.create_assignment(ticket_id, assignment=assignment)


@router.get("/assignments", response_model=list[Assignment])
def get_assignments(db: Session = Depends(get_db)):
    assignment_service: AssignmentService = AssignmentService(db)
    return assignment_service.get_assignments()


@router.get("/assignments/ticket/{ticket_id}", response_model=list[Assignment])
def get_assignments_by_ticket_id(ticket_id: int, db: Session = Depends(get_db)):
    assignment_service: AssignmentService = AssignmentService(db)
    return assignment_service.get_assignments_by_ticket_id(ticket_id=ticket_id)


@router.get("/assignments/task/{task_id}", response_model=list[Assignment])
def get_assignments_by_task_id(task_id: int, db: Session = Depends(get_db)):
    assignment_service: AssignmentService = AssignmentService(db)
    return assignment_service.get_assignments_by_task_id(task_id=task_id)


@router.delete("/assignment/{assignment_id}")
def delete_assignment(assignment_id: int, db: Session = Depends(get_db)):
    assignment_service: AssignmentService = AssignmentService(db)
    return assignment_service.delete_assignment(assignment_id=assignment_id)
