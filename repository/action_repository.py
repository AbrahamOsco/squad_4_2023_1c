from sqlalchemy.orm import Session

from models.data.action import Action


class ActionRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def save(self, db_action: Action):
        self.db.add(db_action)
        self.db.commit()
        self.db.refresh(db_action)
        return db_action

    def find_all(self):
        return self.db.query(Action).all()
