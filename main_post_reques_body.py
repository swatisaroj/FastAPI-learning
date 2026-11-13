# post API
#from fastapi import FastAPI

# app=FastAPI()

# @app.post("/create")
# def create_user(name: str,age: int): # request body se hume kya kya chiz milengi
#     return {
#         "name":name,
#         "age":age
#     }

# json ka data body me kese dikhana hai 
# from fastapi import FastAPI

# app=FastAPI()

# @app.post("/create")
# def create_user(user:dict): json ka data body me kese dikhana hai 
#     return {
#         "message" :"User created",
#         "data":user
#     }


#pydantic 
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int


@app.post("/create")
def create_user(user:User): 
    return {
        "message" :"User created",
        "data":user
    }
