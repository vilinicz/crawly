from pydantic import BaseModel
from pydantic_collections import BaseCollectionModel

from config import SearchEngine


class Entry(BaseModel):
    engine: SearchEngine
    title: str
    url: str


class EntryCollection(BaseCollectionModel[Entry]):
    # Just to eliminate Pycharm "Unexpected argument" warning
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __add__(self, other: "EntryCollection") -> "EntryCollection":
        return EntryCollection(self.root + other.root)
