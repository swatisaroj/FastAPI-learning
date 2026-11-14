from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

#Secure key bna rahe hai signup karne ke liye
SECRET_KEY = "mysecret"
ALGORITHM  = "HS256"

#Create token kiya means function bna rahe hai
def create_token(data:dict):
    to_encode = data.copy()
    # expire = datetime.utcnow()+timedelta 
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)


    to_encode.update({
        "exp":expire
    })

#generate token
    token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return token

#Login API(Token Generate)
@app.post("/login")
def login(username:str, password:str):
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid username and password"
        )

    token = create_token({
        "sub" : username
    })
    return{
        "access_token": token,
        "token_type":"bearer"
    }

#token verify
def verify_token(token: str = Header(None)):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload
    except:
        raise HTTPException(
            status_code= 401,
            detail="Invalid or expired token"
        )

# protected token 
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return{
        "message":"Secure Data Accessed",
        "User":user
    }    



