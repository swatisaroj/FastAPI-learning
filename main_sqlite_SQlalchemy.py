# database integration (sqlite)
# import sqlite3
# from fastapi import FastAPI

# app = FastAPI()

# conn = sqlite3.connect("test.db",check_same_thread=False) #

# cursor = conn.cursor()# sql run

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS todos(
#         id INTEGER PRIMARY KEY,
#         title TEXT,
#         Completed TEXT
#     )
# """)

# conn.commit()

# cursor.execute("""
# SELECT name FROM sqlite_master
# WHERE type = 'table'
# """)

# print(cursor.fetchall())

# @app.get("/") # jo humari fast api hai vo database ke sath connect ho jayge
# def home():
#     return{
#         "message": "SQlite Connected fine"
#     }



# SQLAlchemy database .................
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,declarative_base,session
from fastapi import FastAPI,Depends

# fastapi db se connect karate hai
app = FastAPI()

#Database URL
DATABASE_URL = "sqlite:///./test1.db"

# Engine create (DB connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#Session (DB operation ke liye)
sessionLocal = sessionmaker(bind=engine)

# Base (model ke liye)
Base = declarative_base()


#Tabel(model)
class Todo(Base):# model create kr rahe hai
    __tablename__= "todos"# table ka name diya humne

    id = Column(Integer, primary_key=True, index=True)
    title= Column(String)
    completed= Column(String)

#table create karna database me 
Base.metadata.create_all(bind=engine)

# ek common fun bna dete hai jo check krenga her api me db session mil raha hai ki nh
# Dependency (DB session provide krega) 
def get_db():
    db = sessionLocal() # new db session create kr rahe hai 
    try:
        yield
    finally:
        db.close()

#test api 
@app.get("/")
def home(db: session = Depends(get_db)):
    return{
        "message":"db connected fine"
    }


# next video 17 number CRUD with database 
@app.post("/todos")
def create_todo(title:str, db:session = Depends(get_db)): 
    todo = Todo(title=title, completed="False")  # object create kra
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }
    






