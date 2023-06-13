from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.intentoSolucion import IntentoDeSolucion, IntentoDeSolucionCreate
from services.intentoSolucion_service import IntentoDeSolucionService

router = APIRouter()


@router.post("/intentos",response_model= IntentoDeSolucion)
def createIntento(intento: IntentoDeSolucionCreate, db: Session = Depends(get_db)):
    intento_service: IntentoDeSolucionService = IntentoDeSolucionService(db)
    return intento_service.createIntento(intento=intento)


@router.get("/intentos", response_model=list[IntentoDeSolucion])
def getIntentos(db: Session = Depends(get_db)):
    intento_service: IntentoDeSolucionService = IntentoDeSolucionService(db)
    return intento_service.getIntentos()

@router.get("/ntentos{id}", response_model=IntentoDeSolucion)
def findByID(id : int, db: Session = Depends(get_db) ):
    intento_service: IntentoDeSolucionService = IntentoDeSolucionService(db)
    return intento_service.findById(id=id)
