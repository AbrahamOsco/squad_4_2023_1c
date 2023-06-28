from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import product_controllers, client_controllers, ticket_controllers, assignment_controllers
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_controllers.router)
app.include_router(client_controllers.router)
app.include_router(ticket_controllers.router)
app.include_router(assignment_controllers.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
