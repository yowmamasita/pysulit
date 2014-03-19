#!/usr/bin/env python

from distutils.core import setup

setup(name='pysulit',
      version='1.0.1',
      description='Unofficial Sulit.com.ph SDK for Python',
      author='Ben Sarmiento',
      author_email='me@bensarmiento.com',
      url='https://github.com/yowmamasita/pysulit',
      py_modules=['pysulit.api'],
      requires=['requests', 'beautifulsoup4']
      )
