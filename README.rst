===========
aiocfscrape
===========

A simple async Python module to bypass Cloudflare\'s anti-bot page.
Based on aiohttp ClientSession. Solution was inherited from `cfscrape <https://github.com/Anorov/cloudflare-scrape>`_
module.

You could use it eg. with Python 3 and `asyncio <https://docs.python.org/3/library/asyncio-dev.html>`_
for concurrent crawling of web resources protected with CloudFlare.


.. contents:: Table of Contents


Installation
============

Install with pip

.. code:: sh

    pip install aiocfscrape


Basic Usage
===========

aiocfscrape is a aiohttp.ClientSession wrapper. So `aiohttp client reference <http://aiohttp.readthedocs.io/en/stable/client.html>`_
can be used as the base.

To make simple get request do the following:

.. code:: python

  import asyncio
  from aiocfscrape import CloudflareScraper

  async def test_open_page(url):
      async with CloudflareScraper() as session:
          async with session.get(url) as resp:
              return await resp.text()

  if __name__ == '__main__':
      asyncio.run(test_open_page('<your url>'))


Dependencies
============

- Python `3.5.3+`
- `aiohttp <https://pypi.python.org/pypi/aiohttp>`_ ``>=3.1.3, <4a``
- `js2py <https://pypi.python.org/pypi/Js2Py>`_


License
=======

aiocfscrape is offered under the MIT license.

