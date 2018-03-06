from setuptools import setup

setup(
    name = 'aiocfscrape',
    packages = ['aiocfscrape'],
    version = '0.0.4',
    description = 'A simple async Python module to bypass Cloudflare\'s anti-bot page. See https://github.com/pavlodvornikov/aiocfscrape for more information.',
    author = 'pavlodvornikov',
    author_email = 'pavlodvornikov@gmail.com',
    url = 'https://github.com/pavlodvornikov/aiocfscrape',
    keywords = ['cloudflare', 'scraping', 'asyncio'],
    install_requires = ['js2py==0.50', 'aiohttp >= 2.2.5']
)
