from fastapi import FastAPI

from database.connection import engine, Base
from controllers import product_controllers

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_controllers.router)