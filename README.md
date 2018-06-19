# aiocfscrape
A simple async Python module to bypass Cloudflare\'s anti-bot page. Based on aiohttp ClientSession. Solution was inherited from **cfscrape** module(https://github.com/Anorov/cloudflare-scrape).

This module would be helpful if you use Python3.5 and asyncio for concurrent crawling of web resources protected with CloudFlare.

## Dependencies

* Python 3.5.3+
* **[aiohttp](https://pypi.python.org/pypi/aiohttp)** >= 3.1.3
* **[js2py](https://pypi.python.org/pypi/Js2Py)** == 0.59

Install with pip.

## Basic usage
aiocfscrape is actually aiohttp.ClientSession wrapper. So aiohttp client reference (http://aiohttp.readthedocs.io/en/stable/client.html) can be used as the base.

To make simple get request do the following:

```python
import asyncio
from aiocfscrape import CloudflareScraper

async def test_open_page(url, loop=None):
    async with CloudflareScraper(loop=loop) as session:
        async with session.get(url) as resp:
            data = await resp.text()
    return data

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_open_page('<your url>', loop=loop))
    loop.close()
```

