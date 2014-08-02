
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python implementation of a singly-linked list',
    'author': 'Daniel Pek',
    'url': 'https://github.com/pdani/PyLinkedList',
    'download_url': 'https://github.com/pdani/PyLinkedList',
    'author_email': 'pekdaniel@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['linkedlist'],
    'scripts': [],
    'name': 'PyLinkedList',
    'test_suite': 'tests'
}

setup(**config)
