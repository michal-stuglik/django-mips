django-mips
===========

A simple API (build on top of the Django Model API) to store and manage MIP (molecular inversion probe) markers. 
Detailed markers description e.g in [Science 338, 1619 (2012)].

#### package 
[![PyPI version](https://badge.fury.io/py/django-mips.svg)](http://badge.fury.io/py/django-mips)
[![Code Health](https://landscape.io/github/michal-stuglik/django-mips/master/landscape.svg?style=flat)](https://landscape.io/github/michal-stuglik/django-mips/master)
[![Build Status](https://travis-ci.org/michal-stuglik/django-mips.svg?branch=master)](https://travis-ci.org/michal-stuglik/django-mips)
[![Code Climate](https://codeclimate.com/github/michal-stuglik/django-mips/badges/gpa.svg)](https://codeclimate.com/github/michal-stuglik/django-mips)

Linux
-----

#### apps for Python environment (ubuntu)

    sudo apt-get install python-pip python-dev build-essential libpq-dev python-virtualenv
    
    optional:
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv  

#### download source code & go into it

    git clone https://github.com/michal-stuglik/django-mips.git
    or
    wget https://github.com/michal-stuglik/django-mips/archive/master.zip


#### install django-mips, set virtual environment & requirements

    cd django-mips/
    
    # set isolated virtual environment (VE)
    virtualenv .venv
    
    # source it
    source .venv/bin/activate

    # install required apps within VE
    pip install -r requirements.txt


TODO: Windows
-------------






Setup & usage
-----

#### outside Django project, in python scripts:


make sure you have correct database connection details in mips.dbsettings\_default.py

```
DBNAME = ''  # database-name-on-the-host
USER = ''  # user-name
PASSWORD = ''  # set database-password
HOST = 'xxx.xxx.xxx.xxx'  # set host IP address
SECRET_KEY = 'set-secret-key-here'  # set-secret-key-here

```

go to project directory and load python modules from virtualenv (VE)

```python
source .venv/bin/activate
```


##### In python

set the DJANGO\_SETTINGS\_MODULE environment variable to “mips.settings”

```python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")
```

set up Django

```python
import django
django.setup()
```

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
  [Science 338, 1619 (2012)]: http://www.sciencemag.org/content/338/6114/1619






Old notes
---------


Prerequisites
-------------

####  Python 2.7

Linux
       
    probably, you already have it!
    
Windows

    download & install: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi
	remember to select "Add python.exe to Path"
    
####   pip & virtualenv (optional)

Linux (Ubuntu/Debian)

    sudo apt-get install python-pip python-dev build-essential libpq-dev python-virtualenv
    
    optional:
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
[![Build Status](https://travis-ci.org/michal-stuglik/django-mips.svg?branch=master)](https://travis-ci.org/michal-stuglik/django-mips)
[![Code Climate](https://codeclimate.com/github/michal-stuglik/django-mips/badges/gpa.svg)](https://codeclimate.com/github/michal-stuglik/django-mips)

    https://pypi.python.org/pypi/django-mips


#### source code

    $ git clone https://github.com/michal-stuglik/django-mips.git
    or
    https://github.com/michal-stuglik/django-mips/archive/master.zip


#### with pip (recommended)

Install with pip (you will find mips folder in your local Python directory )

    pip install django-mips
	
Install required modules

    cd django-mips/
    pip install -r requirements.txt


Upgrade
-------

#### with git

    cd django-mips/
    git pull
    pip install -r requirements.txt
    
#### with pip

    pip install -django-mips --upgrade
    cd django-mips/
    pip install -r requirements.txt


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
  [Science 338, 1619 (2012)]: http://www.sciencemag.org/content/338/6114/1619
