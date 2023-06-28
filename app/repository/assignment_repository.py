from sqlalchemy.orm import Session

from app.models.data.assignment import Assignment


class AssignmentRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def save(self, db_assignment: Assignment):
        self.db.add(db_assignment)
        self.db.commit()
        self.db.refresh(db_assignment)
        return db_assignment

    def find_all(self):
        return self.db.query(Assignment).all()

    def find_by_ticket(self, ticket_id: int):
        return self.db.query(Assignment).filter(Assignment.ticket_id == ticket_id).all()

    def find_by_task(self, task_id: int):
        return self.db.query(Assignment).filter(Assignment.task_id == task_id).all()
