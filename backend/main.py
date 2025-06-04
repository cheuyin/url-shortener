from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

url_store = {}  # Maps alias -> original URL

base_url = "https://stanshorts.com/"


class ShortURLRequest(BaseModel):
    original_url: str
    alias: str


@app.get("/api/v1/urls/{alias}")
async def get_original_url(alias: str):
    # Check that the alias is stored
    if alias not in url_store:
        raise HTTPException(status_code=404, detail="URL doesn't exist")

    return {"original_url": url_store[alias]}


@app.post("/api/v1/urls/")
async def create_short_url(request: ShortURLRequest):
    short_url = base_url + request.alias
    url_store[request.alias] = request.original_url
    return {"short_url": short_url}
