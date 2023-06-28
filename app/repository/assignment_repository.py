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
