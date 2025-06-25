from fastapi import FastAPI
from App.routes.hello_route import router as hello_router

app = FastAPI()

app.include_router(hello_router, prefix="/api")