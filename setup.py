import re
import os
from setuptools import setup
from dc import __version__


README = open('README.md').read()


setup(
    name = "dc",
    version = __version__,
    url = "https://github.com/davidmiller/dc",
    description = "Data Catalogue",
    long_description = README,
    install_requires = ['ffs', ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.6",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"
        ],
    packages = ['dc'],
    )
