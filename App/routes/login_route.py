from fastapi import APIRouter, HTTPException
from App.models.login_model import LoginRequest
from App.controllers.login_controller import authenticate_user

router = APIRouter()

@router.post("/login")
def login(req: LoginRequest):
    user_data = authenticate_user(req.userId, req.password)

    if user_data:
        return user_data
    else:
        raise HTTPException(status_code=404, detail="User not found")
