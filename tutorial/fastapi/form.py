from fastapi import FastAPI, Form
from pydantic import BaseModel,EmailStr
app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


class Role(BaseModel):
    name:str
    group_id:str
    permissions:list[str]

class DownloadStatus():
    pass
class Mpoint:
    pass
class MpointElement:
    pass



class OutUser(BaseModel):
    username: str
    full_name: str | None = None
    group_id:str
    roles:Role

class InUser(OutUser):
    password:str
    email:EmailStr

class LoginInfo(BaseModel):
    username:str
    password:str

@app.post("/login",tags=["AuthAPI"])
async def login(userinfo:LoginInfo):
    results = {}
    return NotImplemented
  

@app.post("/users/",status_code=200)
async def create_user(userinfo:InUser)->OutUser:
    results = {}
    return results