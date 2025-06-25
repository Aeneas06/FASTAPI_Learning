from fastapi import FastAPI
from App.routes.login_route import router as login_router

app = FastAPI()
app.include_router(login_router, prefix="/api")
