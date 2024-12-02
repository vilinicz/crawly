import logging
from functools import reduce

import httpx

import search_engines
from search_engines.engine import Engine


class SearchAggregator:
    def __init__(self, engine_names: [], http_client=httpx.AsyncClient()):
        self.logger = logging.getLogger("searcher")
        self.http_client = http_client
        self.engines: list[Engine] = self._init_engines(engine_names)

    def search(self, q: str):
        return reduce(lambda a, b: a + b, [engine.search(q) for engine in self.engines])

    def _init_engines(self, engine_names):
        engines = []
        unknown_engines = []
        for engine_name in engine_names:
            try:
                engines.append(
                    getattr(search_engines, engine_name.capitalize())(self.http_client)
                )
            except AttributeError:
                unknown_engines.append(engine_name)
                continue
        if any(unknown_engines):
            self.logger.warning("Skipping unknown engines: %s", unknown_engines)
        return engines
