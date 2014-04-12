#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import misaka

from reader.markdown import MyRender

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

def md_to_html(text):
    text = to_unicode(text)
    render = MyRender(flags=misaka.HTML_USE_XHTML)
    md = misaka.Markdown(
        render,
        extensions=misaka.EXT_FENCED_CODE | misaka.EXT_AUTOLINK,
    )
    return md.render(text)

