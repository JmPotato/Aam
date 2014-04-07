#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import aam

version = aam.__version__

long_description = open('README.rst').read()

setup(
    name='aam',
    version=version,
    author='JmPotato',
    author_email='ghzpotato@gmail.com',
    url='https://github.com/JmPotato/Aam',
    packages=find_packages(),
    description='a lightweight about me site generator',
    long_description=long_description,
    keywords="Aam, about me, site, static, static page, static site, generator",
    entry_points={
        'console_scripts': ['aam=aam.cli:main'],
    },
    install_requires=open("requirements.txt").readlines(),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)