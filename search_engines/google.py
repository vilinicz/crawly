import logging

from entry import EntryCollection
from search_engines.engine import Engine


class Google(Engine):
    def __init__(self, http_client):
        super().__init__(http_client)
        self.url = "https://google.com"
        self.logger = logging.getLogger("google")

    def search(self, q: str) -> EntryCollection:
        self.logger.info("Searching for %s", q)
        return EntryCollection(
            [
                {"title": f"{q} result {i}", "url": f"https://google.com/{i}"}
                for i in range(1)
            ]
        )
