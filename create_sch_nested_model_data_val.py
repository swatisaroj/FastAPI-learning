#create schema.................
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")
# def create_user(user:User):  
#     return{
#         "message":"User craeted",
#         "data":user
#     }


#.........Nested models.......
from fastapi import FastAPI
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address 

app=FastAPI()      

@app.post("/create_user")
def create_user(user:User):
    return user   