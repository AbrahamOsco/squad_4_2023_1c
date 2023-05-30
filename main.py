from fastapi import FastAPI

from database.connection import engine
from models.data import item, user
from controllers import users
from controllers import items

item.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
