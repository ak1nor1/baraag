#coding: utf-8

from setuptools import setup, find_packages

setup(
    name = 'Baraag',
    version = '0.1dev',
    packages = find_packages(),
    install_requires = [
        'MacFSEvents',
        'moo',
    ],
    author = 'orangain',
    author_email = 'orangain@gmail.com',
    url = 'https://github.com/orangain/baraag',
    long_description = open('README.md').read(),
    keywords = 'evernote markdown preview',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities',
    ],
)