from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.get("/callname/{name}")
def get_name(name: str = None):
    return {"hello": {name}}

class Name(BaseModel):
    name = "rattikan"

@app.post("/callname")
def call_name(name: Name):
    return {"hello": {name}}

handler = Mangum(app)
