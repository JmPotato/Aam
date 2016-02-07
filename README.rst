All About "All about me"
----------------

Aam means "All about me". It is a lightweight about-me-site generator. To compare with a blog, Aam is for pages not posts. So you can use it to build your own resume page.

Installation
===============

Requirements:

* Jinja2
* Mistune
* Pygments
* Parguments

Install Aam with pip ::

    $ (sudo) pip install aam

With Git ::

    $ git clone git://github.com/JmPotato/Aam
    $ cd Aam
    $ (sudo) python setup.py install


Usage
===============

First of all, creat a new site ::

    $ mkdir site
    $ cd site
    $ aam init

Then, edit the config file ::

    $ vim config.ini

You need to have a home page befor a normal page. A home page should like this ::

    title: Welcome
    date: 2014.7.1
    type: home
    ----

    Weclome to Aam!

A normal page named `Hello.md` ::

    title: Hello World
    date: 2014.7.1
    description: The first page
    type: page
    ----

    Hello, World!

Generate the site ::

    $ aam build

Notice
===============

Every page file needs to include four metas.

* title
* date
* description
* type

If you miss any one of them, the site won't be complete.
