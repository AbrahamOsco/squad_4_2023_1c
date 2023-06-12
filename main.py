from fastapi import FastAPI

from database.connection import engine, Base
from controllers import product_controllers, client_controllers
from models.data.product import initialize_db

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_controllers.router)
app.include_router(client_controllers.router)

initialize_db()
