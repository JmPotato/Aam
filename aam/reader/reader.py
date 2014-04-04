#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser

from aam.options import hub
from .markdown import MyRenderer
from aam.utils import to_unicode

def read_config():
    config_path = os.path.join(hub.site.path, 'config.ini')
    if not os.path.exists(config_path):
        print("Can't find any config file.")
        return

    parser = ConfigParser.SafeConfigParser()
    parser.read(config_path)

    hub.site.name = parser.get("settings", "site_name").decode('utf-8')
    hub.site.owner = parser.get("settings", "site_owner").decode('utf-8')
    hub.site.url = parser.get("settings", "site_url").decode('utf-8')

def read_page():
    pass
