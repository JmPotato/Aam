#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

from .utils import *
from .options import *

import aam

doc = """Aam v%s
Usage:
    aam init
    aam build
    aam -h | --help
    aam --version

Options:
    -h --help               Show this screen and exit.
""" % aam.__version__

from parguments import Parguments

parguments = Parguments(doc, version=aam.__version__)

@parguments.command
def init():
    """
    Usage:
        aam init

    Options:
        -h --help               Show this screen and exit.
    """
    hub.root.path = os.path.dirname(__file__)
    hub.root.template_dir = os.path.join(os.path.dirname(__file__),'templates')
    hub.root.static_dir = os.path.join(os.path.dirname(__file__), 'static')
    hub.site.path = os.getcwd()
    shutil.copyfile(os.path.join(hub.root.path, 'config.py'), 'config.py')
    mkdir("pages")
    mkdir("deploy")
    print("Please edit config.py to config your site")

@parguments.command
def build():
    """
    Usage:
        aam build

    Options:
        -h --help               Show this screen and exit.
    """
    pass

def main():
    parguments.run()
