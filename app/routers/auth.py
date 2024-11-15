from fastapi import FastAPI, APIRouter,status
from ..pydantic_models import allSchemas

router = APIRouter(prefix="/user")


#register a user
@router.post("/register",response_class=status.HTTP_201_CREATED)
def create_user(credentials:allSchemas.UserRegister):
    print("User Creation started")