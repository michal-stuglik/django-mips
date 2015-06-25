django-mips
===========

A simple Django app to store and process Mip molecular markers.


Prerequisites
-------------

####  Python 2.7

Linux
       
    probably, you already have it!
    
Windows

    download & install: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi
    
####   pip & virtualenv (optional)

Linux (Ubuntu/Debian)

    sudo apt-get install python-pip python-dev build-essential
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

Windows

    With Python 2.7.10 version, pip is a part of the Python for Windows installer.

Windows alternatively: pip can be downloaded with this script: [get-pip.py], and installed by running in console:

    C:\> python get-pip.py



Requirements
------------
    
####   Django 1.7-1.8
    
    pip install django


####   Python-PostgreSQL Database Adapter

Linux

    pip install psycopg2
    
    
Windows
     
     pip install git+https://github.com/nwcell/psycopg2-windows.git@win32-py27#egg=psycopg2
     
     
Windows alternatively: download & install from win-psycopg project site -  e.g. [psycopg2]
          
     http://stickpeople.com/projects/python/win-psycopg/
     


Download
--------

#### package 
[![PyPI version](https://badge.fury.io/py/django-mips.svg)](http://badge.fury.io/py/django-mips)
[![Code Health](https://landscape.io/github/michal-stuglik/django-mips/master/landscape.svg?style=flat)](https://landscape.io/github/michal-stuglik/django-mips/master)

    https://pypi.python.org/pypi/django-mips


#### source code

    $ git clone https://github.com/michal-stuglik/django-mips.git


#### with pip (recommended)

Install with pip

    pip install django-mips


Setup
-----

#### outside Django project, in python scripts:


*   set database connection details in mips.dbsettings\_default.py
*   set the DJANGO\_SETTINGS\_MODULE environment variable to “mips.settings”


    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

*   set up Django: django.setup()


    import django
    django.setup()

Examples
--------

[scripts & README]

  [get-pip.py]: https://raw.github.com/pypa/pip/master/contrib/get-pip.py
  [image]: https://pypip.in/v/django-mips/badge.png
  [1]: https://pypip.in/d/django-mips/badge.png
  [scripts & README]: https://github.com/michal-stuglik/django-mips/tree/master/mips/example
  [psycopg2]: http://stickpeople.com/projects/python/win-psycopg/2.6.0/psycopg2-2.6.0.win32-py2.7-pg9.4.1-release.exe
  [pythonwin]: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi
  [django-mips]: https://pypi.python.org/pypi/django-mips
