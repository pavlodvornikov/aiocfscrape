from setuptools import find_packages, setup

version = '0.0.10.dev0'


long_description = '{}\n\n{}'.format(open('README.rst').read(),
                                     open('CHANGES.rst').read())

setup(name='aiocfscrape',
      version=version,
      description='A simple async Python module to bypass Cloudflare\'s anti-bot page. '
                  'See https://github.com/pavlodvornikov/aiocfscrape for more information.',
      long_description=long_description,

      author='pavlodvornikov',
      maintainer='Nachtalb',
      url='https://github.com/pavlodvornikov/aiocfscrape',
      license='MIT',

      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'js2py',
          'aiohttp >= 3.1.3, <4a',
      ],
      )
