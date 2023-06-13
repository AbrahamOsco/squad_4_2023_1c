from fastapi import FastAPI

from database.connection import engine, Base
from controllers import product_controllers, intentoSolucion_controllers

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_controllers.router)
app.include_router(intentoSolucion_controllers.router)