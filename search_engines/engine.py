from entry import EntryCollection


class Engine:
    def __init__(self, http_client):
        self.http_client = http_client

    def search(self, q: str) -> EntryCollection:
        raise NotImplementedError("search method must be implemented in subclasses")
