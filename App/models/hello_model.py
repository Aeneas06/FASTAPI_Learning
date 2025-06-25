from pydantic import BaseModel

class HelloRequest(BaseModel):
    q: str
