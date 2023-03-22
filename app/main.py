from fastapi import FastAPI
from mangum import Mangum
name = None

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
    global names
    names = name
    return {"hello": {name}}

@app.post("/callname")
def call_name():
    return {"hello": {names}}

handler = Mangum(app)
