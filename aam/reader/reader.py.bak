#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import urllib2
import datetime
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

    hub.site.name = parser.get("main_settings", "site_name").decode('utf-8')
    hub.site.owner = parser.get("main_settings", "site_owner").decode('utf-8')
    hub.site.url = parser.get("main_settings", "site_url").decode('utf-8')
    hub.site.github_name = parser.get("main_settings", "github_name").decode('utf-8')
    hub.site.douban_name = parser.get("main_settings", "douban_name").decode('utf-8')
    hub.site.analytics = parser.get("main_settings", "analytics").decode('utf-8')

    hub.site.repo_switch = parser.getboolean("function_switch", "show_github_repo")
    hub.site.book_switch = parser.getboolean("function_switch", "show_douban_book")

def read_page():
    page_list = []
    if not os.path.exists(hub.site.page_path):
        print("Can't find any page. Please make sure you have built a site environment.")
        print("You can use \'aam -h\' to get help")
        exit(1)
    all_pages = os.listdir(hub.site.page_path)
    os.chdir(hub.site.page_path)
    for page in all_pages:
        try:
            if page.split('.')[1] != 'md':
                continue
        except:
            pass
        page_content = {"title": "", "date": "", "description": "", "type": "","content": "", "link": ""}
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
    hub.site.pages = sorted(page_list, key = lambda x:x['title'][0])
    get_github_repo()

def get_github_repo():
    repo_list = []
    all_repos = json.JSONDecoder().decode(urllib2.urlopen('https://api.github.com/users/%s/repos' % hub.site.github_name).read())
    for repo in all_repos:
        repo_content = {"name": "","star": "","url": "","description": ""}
        repo_content["name"] = repo["name"]
        repo_content["star"] = repo["stargazers_count"]
        repo_content["url"] = repo["html_url"]
        repo_content["description"] = repo["description"]
        repo_list.append(repo_content)
    hub.site.github_repo = repo_list
