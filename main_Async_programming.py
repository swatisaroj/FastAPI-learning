#sync programming
# import time

# def task():
#     time.sleep(3)
#     return "Done"


#Async programming
# import asyncio

# async def task():
#     await asyncio.sleep(3)
#     return "Done"




#Async programming with fastapi......................
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Async API"
    }

















