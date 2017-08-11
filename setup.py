#!/usr/bin/env python3
# coding: utf-8
from setuptools import setup, find_packages
from pip_github_test import __author__, __version__, __license__

setup(
    name='easy_mongo',
    version=__version__,
    description='easy mongodb',
    license=__license__,
    author=__author__,
    author_email='crawd4274@gmail.com',
    url='https://github.com/takashiAg/easy_mongo_python',
    keywords='sample pip github python',
    packages=find_packages(),
    install_requires=[],
)