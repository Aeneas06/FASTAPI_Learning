from App.models.hello_model import HelloRequest

def say_hello(request: HelloRequest):
    if request.q.lower() == "hi":
        return {"message": "Hello world"}
    return {"message": "Say hi to get a proper greeting!"}
