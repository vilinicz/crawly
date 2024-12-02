import logging
from typing import TypeVar, Generic, Annotated, Optional, get_args

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing_extensions import Literal

from entry import EntryCollection
from search_aggregator import SearchAggregator

logger = logging.getLogger(__name__)
app = FastAPI()

SearchEngine = Literal["google", "bing"]

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
    fake_results = SearchAggregator(params.engines).search(params.q)
    return GenericResponse(data=fake_results, meta={"params": params})
