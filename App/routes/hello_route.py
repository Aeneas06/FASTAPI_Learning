from fastapi import APIRouter
from App.controllers.hello_controller import say_hello
from App.models.hello_model import HelloRequest

router = APIRouter()

@router.post("/hello")
def hello_endpoint(body: HelloRequest):
    return say_hello(body)

@router.get("/hello")
def hello_get_endpoint():
    return {"message": "Hello world"}
