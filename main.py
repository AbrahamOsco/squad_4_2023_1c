from fastapi import FastAPI

from database.connection import engine, Base
from controllers import users
from controllers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
