#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mistune

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class MyRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

    def autolink(self, link, is_email):
        if is_email:
            mailto = "".join(['&#%d;' % ord(letter) for letter in "mailto:"])
            email = "".join(['&#%d;' % ord(letter) for letter in link])
            url = mailto + email
            return '<a href="%(url)s">%(link)s</a>' % {'url': url, 'link': email}

        title = link.replace('http://', '').replace('https://', '')
        if len(title) > 30:
            title = title[:24] + "..."
        return '<a href="%s">%s</a>' % (link, title)
