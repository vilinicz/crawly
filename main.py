import logging
from typing import TypeVar, Generic, Annotated, Optional, get_args

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI, Query
from pydantic import BaseModel

from config import SearchEngine
from entry import EntryCollection
from search import Aggregator

logger = logging.getLogger(__name__)
app = FastAPI()
app.add_middleware(CorrelationIdMiddleware)


T = TypeVar("T")


class GenericResponse(BaseModel, Generic[T]):
    data: T
    meta: Optional[dict] = None


class SearchParams(BaseModel):
    q: str = Query(None, description="Your search query")
    engines: list[SearchEngine] = get_args(SearchEngine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search")
async def search(
    params: Annotated[SearchParams, Query()],
) -> GenericResponse[EntryCollection]:
    results = await Aggregator(params.engines).search(params.q)
    return GenericResponse(data=results, meta={"params": params})
