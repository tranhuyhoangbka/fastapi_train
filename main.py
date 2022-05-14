from pydoc import describe
from fastapi import FastAPI
from typing import Optional
from fastapi.params import Query
from deta import Deta
from pydantic import BaseModel

app = FastAPI()
deta = Deta('c0onrnyn_UxdzwAhpr8D1DkcLWkhLjCniW3BehtfB')
db = deta.Base('todos')

class CreateTodoModel(BaseModel):
    title: str
    description: str
    completed: bool

class UpdateTodoModel(BaseModel):
    key: str
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None



@app.get("/")
async def index():
    # users = deta.Base("users")

    # users.insert({
    #     "name": "Geordi",
    #     "title": "Chief Engineer"
    # })
    return "Hello world"

@app.get("/todos")
async def get_todos(completed: Optional[bool] = Query(None, description = "is todo completed")):
    if (completed == None):
        completed = False
    todos = db.fetch({"completed": completed})
    return todos.items

@app.post('/todos')
async def create_todo(model: CreateTodoModel):
    todo = db.put(model.dict())
    return todo

@app.put('/todos')
async def update_todo(model: UpdateTodoModel):
    todo = db.put(model.dict())
    return todo

@app.delete('/todos/{key}')
async def delete_todo(key: str):
    db.delete(key=key)
    return {"success": True}