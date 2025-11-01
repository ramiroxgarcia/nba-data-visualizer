import uvicorn

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from nba_data_provider import NbaDataProvider

app = FastAPI()

ndp = NbaDataProvider()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/api")
def read_root():
    return {"players": ndp.get_players()}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/api/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)