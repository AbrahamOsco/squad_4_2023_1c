from fastapi import FastAPI

from app.controllers import product_controllers, client_controllers, ticket_controllers, action_controllers
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_controllers.router)
app.include_router(client_controllers.router)
app.include_router(ticket_controllers.router)
app.include_router(action_controllers.router)
