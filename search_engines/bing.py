import logging

from entry import EntryCollection
from search_engines.engine import Engine


class Bing(Engine):
    def __init__(self, http_client):
        super().__init__(http_client)
        self.url = "https://bing.com"
        self.logger = logging.getLogger("bing")

    def search(self, q: str) -> EntryCollection:
        self.logger.info("Searching for %s", q)
        return EntryCollection(
            [
                {"title": f"{q} result {i}", "url": f"https://bing.com/{i}"}
                for i in range(1)
            ]
        )
