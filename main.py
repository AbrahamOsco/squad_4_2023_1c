from fastapi import FastAPI

from database.connection import engine, Base
from controllers import account_controllers, transaction_controllers

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(account_controllers.router)
app.include_router(transaction_controllers.router)
