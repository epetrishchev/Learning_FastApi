from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get('/')
def read_root():
    return {'Hello': 'World!'}


@app.get('/items/{item_id}')
def reat_item(item_id: int, q: str | None = Query(default=None, min_length=3, max_length=50)):
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}
