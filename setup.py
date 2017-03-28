#!/usr/bin/env python

"Setuptools params"

from setuptools import setup, find_packages

VERSION = '0.1'

modname = distname = 'minigenerator'

def readme():

    with open('README.md','r') as f:
        return f.read()

setup(
    name=distname,
    version=VERSION,
    description='Simple traffic generator for mininet networks',
    author='Edgar Costa',
    author_email='cedgar@ethz.ch',
    packages=find_packages(),
    long_description=readme(),
    include_package_data = True,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python 2.7",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Networking",
        ],
    keywords='networking OSPF mininet',
    license='GPLv2',
    install_requires=[
        'setuptools',
        'networkx'
    ],
    extras_require={},
    tests_require=['pytest'],
    setup_requires=['pytest-runner']
)
