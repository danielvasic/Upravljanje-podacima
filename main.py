from fastapi import FastAPI
from pydantic import BaseModel
from models import db
from models.program import Program

app = FastAPI()

class ProgramItem (BaseModel):
    name : str
    version : str
    description : str

@app.get("/")
def index ():
    return {"message": "Hello, World!"}

@app.get("/item/{item_id}")
def get_item(item_id:int):
    return {"item_id": item_id}

@app.post("/item/add")
def add_item(item : ProgramItem):
    program = Program(name=item.name, version=item.version, description=item.description)
    db.add(program)
    db.commit()
    return {"item": item}

@app.get("/items/programs")
def get_programs() -> list[ProgramItem]:
    return db.query(Program).all()