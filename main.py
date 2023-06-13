from fastapi import FastAPI

from database.connection import engine, Base
from controllers import product_controllers, client_controllers, ticket_controllers, action_controllers

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_controllers.router)
app.include_router(client_controllers.router)
app.include_router(ticket_controllers.router)
app.include_router(action_controllers.router)
