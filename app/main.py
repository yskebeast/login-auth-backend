from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    a = 1
    b = 2
    c = a + b
    return {"message": "Hello World"}
