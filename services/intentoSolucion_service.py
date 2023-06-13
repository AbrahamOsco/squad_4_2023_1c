from fastapi import HTTPException

from sqlalchemy.orm import Session

from models.data.intentoSolucion import IntentoDeSolucion
from models.request.intentoSolucion import IntentoDeSolucionCreate
from repository.intentoSolucion_repository import IntentoDeSolucionRepository


class IntentoDeSolucionService:
    def __init__(self, db: Session):
        self.intentoDeSolucionRepository = IntentoDeSolucionRepository(db)

    def createIntento(self, intento: IntentoDeSolucionCreate):
        db_intento = IntentoDeSolucion(descripcion=intento.descripcion)
        return self.intentoDeSolucionRepository.guardarIntento(db_intento)

    def getIntentos(self):
        return self.intentoDeSolucionRepository.findAll()

    def findById(self, id: int):
        db_intento: IntentoDeSolucion = self.intentoDeSolucionRepository.findById(id)
        if db_intento is None:
            raise HTTPException(status_code=404, detail="Account not found")
        return db_intento
