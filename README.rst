All About "All about me"
----------------

Aam means "All about me". It is a lightweight about me site generator. To compare with blog, Aam is for pages not posts. So you can use it to build your own pages to introduce everything about you.

Installation
===============

Requirements:

* Jinja2
* Mistune
* Pygments
* Parguments

Install Aam with pip ::

    $ (sudo) pip install aam

Or you can install with Git ::

    $ git clone git://github.com/JmPotato/Aam
    $ cd Aam
    $ (sudo) python setup.py install


Usage
===============

First, you need to creat a new site ::

    $ mkdir site
    $ cd site
    $ aam init

Then, edit the config file ::

    $ vim config.ini

You need to build a home page befor writing a page. A home page is like this ::

    title: Welcome
    date: 2014.7.1
    type: home
    ----

    Weclome to Aam!

Write a page like this and save it to `Hello.md` ::

    title: Hello World
    date: 2014.7.1
    description: The first page
    type: page
    ----

    Hello, World!

Build your about me site ::

    $ aam build

Notice
===============

Every page file needs to have all the metas, it includes

* title
* date
* description
* type

If you miss any one of them, your site will be incomplete.