#!/usr/bin/env python
from setuptools import setup, find_packages

def parse(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

requirements = lambda f: [str(i) for i in parse(f)]

setup(
    name='PyNFe',
    version='0.2',
    packages=find_packages(),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    install_requires=requirements('requirements.txt'),
    zip_safe=False,
)
