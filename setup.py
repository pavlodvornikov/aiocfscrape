from setuptools import setup

setup(
  name = 'aiocfscrape',
  packages = ['aiocfscrape'],
  version = '0.0.1',
  description = 'A simple async Python module to bypass Cloudflare\'s anti-bot page. See https://github.com/Anorov/cloudflare-scrape for more information.',
  author = 'Anorov',
  author_email = 'anorov.vorona@gmail.com',
  url = 'https://github.com/Anorov/cloudflare-scrape',
  keywords = ['cloudflare', 'scraping'],
  install_requires = ['Js2Py==0.37', 'requests >= 2.0.0']
)