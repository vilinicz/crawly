import asyncio
import logging

from bs4 import BeautifulSoup

from entry import EntryCollection
from search.engine import Engine


class Google(Engine):
    def __init__(self, http_client):
        super().__init__(http_client)
        self.url = "https://www.google.com/search"
        self.logger = logging.getLogger("google")

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
        div_tags = soup.body.find_all("div", class_="g")
        link_tags = [div.find("a") for div in div_tags]
        links: list[dict] = []
        for link in link_tags:
            title = link.find("h3").text
            url = link.get("href")
            if not any(item["url"] == url and item["title"] == title for item in links):
                links.append(
                    {
                        "engine": self.__class__.__name__.lower(),
                        "title": link.find("h3").text,
                        "url": link.get("href"),
                    }
                )
        return links
