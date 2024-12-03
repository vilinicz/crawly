import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "authority": "www.google.com",
    "Cookie": "AEC=AZ6Zc-XhLv-TOcUV5nktjBA3lb8uUM-Isq3Nv0QqMOPWRW7-ILg5OyiJzA; SOCS=CAISHAgCEhJnd3NfMjAyNDExMjYtMF9SQzEaAm5sIAEaBgiAlLm6Bg; NID=519=F_pSyOUcs2wVQ-5aU8ggotrGEtcstvf9oLEw0F7Yf5BOjP9tX9ZrYqBmVjjlBkVJLq_wJePqnlgP8dlvlY6lcGugTZBWU_UN3PYT8hDTO0VX35H-7cFwhqSeMiM9Kf7AlXPMGQHjy2PWtYyTSKQGETTLqipc_V5JzxTQByoLq2Yjupy9hmtpNVytaX1cZfvOPhn5YI_HhY3ZJK13xtsdaVIYTgQ9TtIb9mw4Yvxim4YYaiqeQgKa; DV=Q7rDc4E0MeITMLoqspk1c5HHZ53TOBk",
}


def default_http_client():
    return httpx.AsyncClient(
        timeout=5, headers=headers, follow_redirects=True, http2=True
    )
