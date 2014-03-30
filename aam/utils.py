#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def to_unicode(value):
    if isinstance(value, unicode):
        return value
    if isinstance(value, basestring):
        return value.decode('utf-8')
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
