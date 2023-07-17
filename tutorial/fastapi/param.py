from fastapi import FastAPI,Query
from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]






@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_item(item_id:int,skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

