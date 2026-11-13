from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

#put users/101?notify=true.....101=>path param......notify=true=>query params
# {
#     "name" : "swati",..................ye hai request body ye teeno chiz ek he api me teeno i/o work kregnge
#     "age": 23
# }
users =[]

class User(BaseModel):
    name:str
    age:int


@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message":"user created",
        "data":user
    }

@app.put("/users/{user_id}")
def updated_user(user_id:int,user:User,notify:bool= False):
    print("Users list:", users)
    print("Requested ID:", user_id)
    print("Users count:", len(users))
    if user_id < len(users):
        users[user_id]= user

        return{
            "message":"user updated",
            "notify":notify,
            "data":user
        }

    return{
        "error":"User not found"
    }