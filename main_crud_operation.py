#CRUD create post api
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[] #.....ek variable liya hai jisme list ko store krayenge

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"TODO added",
        "data":todo
    }

@app.get("/todos")# get api 
def get_todos():
    return todos

# Read opeartion only to specific data using path params
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if(todo.id == todo_id):
            return todo
    return {"error":"Todo not found"}  

# update operation   
@app.put("/todos{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "message":"Data Updated",
                "data":updated_todo
            }
    return {"error":"Todo not found"}   

# delete operation
@app.delete("/todos{todo_id}")
def delete_todo (todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todo.pop(index)
            return {"message":"Data Deleted"}
    return {"error":"Todo not found"}    

