#!/usr/bin/env python
from setuptools import setup

VERSION = "0.1"
REPO = "https://github.com/icio/tarnish"
README = "README.md"

with open(README) as f:
    long_description = f.read()

setup(
    name="tarnish",
    version=VERSION,
    description="Can't handle my tarn",
    author="Paul Scott, Duedil Limited",
    author_email="paul@duedil.com",
    url=REPO,
    download_url="%s/tarball/%s" % (REPO, VERSION),
    py_modules=["tarnish"],
    license="MIT",
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'tarnish = tarnish:main',
        ],
    },
    keywords=["tarnfeld", "tarnfeid", "tarn", "can't handle my"],
    classifiers=[],
)
