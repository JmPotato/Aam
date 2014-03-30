#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import aam

version = aam.__version__

setup(
    name='aam',
    version=version,
    author='JmPotato',
    author_email='ghzpotato@gmail.com',
    url='https://github.com/JmPotato/Aam',
    packages=find_packages(),
    description='Aam: a lightweight about me site generator',
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