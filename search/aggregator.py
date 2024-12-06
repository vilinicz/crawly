import asyncio
import logging
from functools import reduce

import search as search_engines
from search.config import default_http_client
from search.engine import Engine


class Aggregator:
    def __init__(self, engine_names: [], http_client=default_http_client):
        self.logger = logging.getLogger("searcher")
        self.http_client = http_client
        self.engines: list[Engine] = self._init_engines(engine_names)

    async def search(self, q: str):
        results = asyncio.gather(*[engine.search(q) for engine in self.engines])
        return reduce(lambda x, y: x + y, await results)  # Merge results

    def _init_engines(self, engine_names):
        engines = []
        unknown_engines = []

        def engine_name_to_pascal_case(name):
            words = name.split("_")
            return "".join([word.capitalize() for word in words])

        for engine_name in engine_names:
            try:
                engines.append(
                    getattr(search_engines, engine_name_to_pascal_case(engine_name))(
                        self.http_client
                    )
                )
            except AttributeError:
                unknown_engines.append(engine_name)
                continue
        if any(unknown_engines):
            self.logger.warning("Skipping unknown engines: %s", unknown_engines)
        return engines
