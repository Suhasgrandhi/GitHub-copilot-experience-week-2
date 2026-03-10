from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample", "price": 9.99, "is_offer": False}
