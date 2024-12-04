import asyncio
import logging

from bs4 import BeautifulSoup

from entry import EntryCollection
from search.engine import Engine


class Bing(Engine):
    def __init__(self, http_client):
        super().__init__(http_client)
        self.url = "https://bing.com/search"
        self.logger = logging.getLogger("bing")

    async def search(self, q: str) -> EntryCollection:
        self.logger.info("Searching for %s", q)
        async with self.http_client() as client:
            response = await client.get(self.url, params={"q": q})
        return EntryCollection(await self._extract_links(response))

    async def _extract_links(self, response):
        loop = asyncio.get_event_loop()
        soup = await loop.run_in_executor(
            None, BeautifulSoup, response.text, "html.parser"
        )
        li_tags = soup.find_all("li", class_="b_algo")
        links = []
        for li_tag in li_tags:
            link = li_tag.find("h2").find("a")
            links.append(
                {
                    "engine": self.__class__.__name__.lower(),
                    "title": link.text,
                    "url": link.get("href"),
                }
            )
        return links
