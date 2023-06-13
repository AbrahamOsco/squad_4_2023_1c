from sqlalchemy.orm import Session

from models.data.intentoSolucion import IntentoDeSolucion


class IntentoDeSolucionRepository:
    def __init__(self, sess: Session):
        self.db: Session = sess

    def guardarIntento(self, intento: IntentoDeSolucion):
        self.db.add(intento)
        self.db.commit()
        self.db.refresh(intento)
        return intento

    def findById(self, id: int):
        return self.db.query(IntentoDeSolucion).get(id)

    def findAll(self):
        return self.db.query(IntentoDeSolucion).all()

