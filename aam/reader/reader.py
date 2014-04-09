#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import ConfigParser

from StringIO import StringIO

from aam.utils import md_to_html
from aam.options import hub

def read_config():
    config_path = os.path.join(hub.site.path, 'config.ini')
    if not os.path.exists(config_path):
        print("Can't find any config file.")
        exit(1)

    parser = ConfigParser.SafeConfigParser()
    parser.read(config_path)

    hub.site.name = parser.get("settings", "site_name").decode('utf-8')
    hub.site.owner = parser.get("settings", "site_owner").decode('utf-8')
    hub.site.url = parser.get("settings", "site_url").decode('utf-8')

def read_page():
    page_list = []
    if not os.path.exists(hub.site.page_path):
        print("Can't find any page. Please make sure you have built a site environment.")
        print("You can use \'aam -h\' to get help")
        exit(1)
    all_pages = os.listdir(hub.site.page_path)
    os.chdir(hub.site.page_path)
    for page in all_pages:
        if page.split('.')[1] != 'md':
            continue
        page_content = {"title": "", "date": "", "description": "","content": "", "link": ""}
        p = open(page).read()
        metas = p.split('----')[0].strip()
        for meta in StringIO(metas):
            try:
                name, value = meta.split(':')
                name = name.strip().lower()
                page_content[name.strip()] = value.strip()
            except:
                pass
        page_content["link"] = os.path.splitext(page)[0].replace(' ','') + '.html'
        page_content["content"] = md_to_html(p.split('----')[1].strip())
        page_list.append(page_content)
    hub.site.pages = page_list
