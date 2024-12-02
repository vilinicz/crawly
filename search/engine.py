from entry import EntryCollection
from search.config import default_http_client


class Engine:
    def __init__(self, http_client=default_http_client):
        self.http_client = http_client

    async def search(self, q: str) -> EntryCollection:
        raise NotImplementedError("search method must be implemented in subclasses")
