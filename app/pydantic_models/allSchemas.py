from pydantic import BaseModel
from typing import Optional

class UserRegister(BaseModel):
    email:str
    password:str
    previous_company:Optional[str]=None