#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class DictSpace(dict):
    def __getattr__(self, key):
        if key in self:
            return self[key]
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except:
            raise AttributeError

hub = DictSpace()
hub.root = DictSpace()
hub.site = DictSpace()
