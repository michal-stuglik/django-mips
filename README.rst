django-mips
===========

A simple Django app to store and process Mip molecular markers.


Prerequisites
-------------

pip & virtualenv (optional)

Linux (Ubuntu/Debian)

::

    sudo apt-get install python-pip python-dev build-essential
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

Windows

    With Python 2.7.10 version, pip is a part of the Python for Windows installer;
    alternatively pip can be downloaded with this script: `get-pip.py <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_,
    and installed by running in console

::

    C:\> python get-pip.py


Requirements
------------

1. Python 2.7
2. Django 1.7-1.8

::

    pip install django


3. Python-PostgreSQL Database Adapter

::

    pip install psycopg2

    windows
    http://stickpeople.com/projects/python/win-psycopg/


Download as a package
---------------------

.. image:: https://pypip.in/v/django-mips/badge.png
:target: https://pypi.python.org/pypi/django-mips

.. image:: https://pypip.in/d/django-mips/badge.png
:target: https://pypi.python.org/pypi/django-mips


Download as a source code
-------------------------

::

    $ git clone https://github.com/michal-stuglik/django-mips.git


Download, install with pip (recommended)
----------------------------------------

Install with pip

::

    pip install django-mips


Usage: outside Django project, within python scripts
----------------------------------------------------

1. set database connection details in mips.dbsettings_default.py
2. set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"

::

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")


3. set up Django: django.setup()

::

    import django
    django.setup()


Examples
--------

`scripts & README <https://github.com/michal-stuglik/django-mips/tree/master/mips/example>`_



..
    Quick start: inside Django project
    ----------------------------------

    1. Modify/set database connection details in mips.dbsettings_default.py
    2. Add "mips" to your INSTALLED_APPS setting like this

    ::

        INSTALLED_APPS = (
            'mips',
        )


    3. Include the polls URLconf in your project urls.py like this

    ::

        url(r'^mips/', include('mips.urls')),



