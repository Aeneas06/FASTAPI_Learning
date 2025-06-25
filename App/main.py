# app/main.py
from fastapi import FastAPI
from App.routes import user_route
from App.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_route.router)
