#HTTPException means hum easily handle kr sakte hai exception ko api ke andar
# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code= 404,
#             detail="User Not Found"
#         )
#     return{
#         "id":1,
#         "name":"aryan"
#     }

#custom Exception kese handel kronge..custom exception error function bnana pfhta hai ek bar code likho
#multiple time use kro 
from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception): # custom error bna rahe hai 
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)# global exception handler bnaya hai 
def user_not_found(request:Request, exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )        

@app.get("/user/{name}")
def get_user(name:str):
    if name!= "mohit":
        raise UserNotFoundException(name)
    return{
        "name":name
    }
