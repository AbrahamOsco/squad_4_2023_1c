from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models.request.transaction import Transaction
from services.transaction_service import TransactionService

router = APIRouter()


@router.get("/transactions", response_model=list[Transaction])
def get_accounts(db: Session = Depends(get_db)):
    transaction_service: TransactionService = TransactionService(db)
    return transaction_service.get_transactions()


