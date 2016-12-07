import os
from setuptools import setup

setup(
    name = 'Image cryptography',
    version = '0.1.0',
    description = ('Implementation of image cryptography'),
    packages = ['crypto'],
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
)