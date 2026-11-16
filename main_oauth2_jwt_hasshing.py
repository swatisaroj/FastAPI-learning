from fastapi import FastAPI, HTTPException,Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

#JWT Config
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =30

#password hasing setup
# passlib password hashing manage karta hai.
# bcrypt actual password hashing operation perform karta hai.
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

# oauthsetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy user database
fake_user_db = {
    "admin":{
        "username":"admin",
        "hashed_password" : pwd_context.hash("1234")
    }
}

#Hash password
def hash_password(password:str):
    return pwd_context.hash(password)


#verify password
def verify_password(plain_password: str,hashed_password: str):
    return pwd_context.verify(plain_password,hashed_password)


#Create token kiya means function bna rahe hai
def create_token(data:dict):
    to_encode = data.copy()
    #expire = datetime.utcnow()+timedelta 
    expire = datetime.now(timezone.utc) + timedelta( minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


    to_encode.update({
        "exp":expire
    })

#generate token 
    token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)    
    return token

#LOGIN API (oauth2 form)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm= Depends()):
    user = fake_user_db.get(form_data.username)

    if not user or not verify_password(

        form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or passowrd"
        )
    
    access_token = create_token({"sub" : form_data.username})
    return{
        "access_token" : access_token,
        "token_type":"bearer"
    }

# token verify
def verify_token(token:str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM]
            )
        
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        
        return username
    
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

#protected Route
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return{
        "message":"Hello you have access to this protected route!",
        "user":username
    }    