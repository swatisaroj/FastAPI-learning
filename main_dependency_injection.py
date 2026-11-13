#what is depends
from fastapi import FastAPI, Depends,Header,HTTPException


app=FastAPI()

# def common_logic():
#     return{
#         "message":"Common Logic executed"
#     }

# @app.get("/home")
# def home(data= Depends(common_logic)):
#     return data

#reusable logic
# def get_current_user():
#     return{
#         "name":"mohit"
#     }
# @app.get("/profile")
# def profile(user= Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def dashboard(user= Depends(get_current_user)):
#     return user


# Auth exp intro 
def verify_token(token:str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return{
        "user":"Authorized User"
    }

@app.get("/secure_data")
def secure_data(user = Depends(verify_token)):
    return {
        "message":"Secure data accessed",
        "user":user
    } 