import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    logger.debug("Name: %s", name)
    return {"message": f"Hello {name}"}
