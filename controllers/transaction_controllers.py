from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.transaction import Transaction
from services.transaction_service import TransactionService

router = APIRouter()


@router.get("/transactions", response_model=list[Transaction])
def get_transactions(db: Session = Depends(get_db)):
    transaction_service: TransactionService = TransactionService(db)
    return transaction_service.get_transactions()


@router.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction_service: TransactionService = TransactionService(db)
    return transaction_service.find_by_id(transaction_id=transaction_id)


@router.get("/transactions/cbu/{cbu}", response_model=list[Transaction])
def get_transactions(cbu: int, db: Session = Depends(get_db)):
    transaction_service: TransactionService = TransactionService(db)
    return transaction_service.find_by_cbu(cbu=cbu)
