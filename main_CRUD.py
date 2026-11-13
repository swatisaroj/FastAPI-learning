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
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

# fastapi db se connect karate hai
app = FastAPI()

#Database URL
DATABASE_URL = "sqlite:///./test2.db"

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
    status= Column(String)

#table create karna database me 
Base.metadata.create_all(bind=engine)

# ek common fun bna dete hai jo check krenga her api me db session mil raha hai ki nh
# Dependency (DB session provide krega) 
def get_db():
    db = sessionLocal() # new db session create kr rahe hai 
    try:
        yield db
    finally:
        db.close()

#test api 
@app.get("/")
def home(db: Session = Depends(get_db)):
    return{
        "message":"db connected fine"
    }


# next video 17 number CRUD with database create operation
@app.post("/todos")
def create_todo(title:str, db: Session = Depends(get_db)): 
    todo = Todo(title=title, status="False")  # object create kra
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }
    
# next video 18 number CRUD with database read operation
# Read all data
@app.get("/todos")
def get_todos(db:Session= Depends(get_db)):
    todos = db.query(Todo).all()

    return{
        "total":len(todos),
        "data":todos
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db:Session= Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo 


# next video 19 number CRUD with database update data operation
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title:str, db:Session= Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id ).first()  

    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    todo.title = title

    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Updated",
        "data":todo
    }


# CRUD with database delete - remove data
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db:Session =Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException (status_code=404, detail="todo not found")

    db.delete(todo)

    db.commit()

    return{
        "message":"Todo deleted"
    }









