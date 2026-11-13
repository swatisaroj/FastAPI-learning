# from fastapi import FastAPI

# app = FastAPI()
# Home Route only show home page
# @app.get("/")
# def home():
#     return{"message":"Welcome to FastApi"}


#About Route
# @app.get("/about")
# def about():
#     return{"Message": "This is about page"}

#Users Route
# @app.get("/users")
# def users():
#     return{
#         "users":["Swati","aryan","pawan","swati"]
#     }

#Dynamic user route int,str data type
# @app.get("/users/{user_id}")
# def get_users(user_id:int):
# def get_users(user_id:str):
#     return {"user_id": user_id}

# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/users")
# def get_users(name):
#     return{"Name":name}


#optional parameters
# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/users")
# def get_users(name: str = None):
#     return {"Name":name}

#Default parameter
# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/products")
# def get_users(limit: int = 10):
#     return {"limit":limit}

#Multiple query parameters
# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/items")
# def get_items(name : str = None, price : int = 0 ):
#     return {
#         "name":name,
#         "price":price
#     }



