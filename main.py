from fastapi import FastAPI, HTTPException, Response

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "There goes my error"})
    return {"item": items[item_id]}


@app.get("/hello")
def read_root():
    response = Response(content="Hello, world!", media_type="text/plain")
    response.headers["X-Custom-Header"] = "My custom header"
    return response
    # return {"name": "john"}

# second commit

# third commit
