"""Database settings file"""

DBNAME = ''  # database-name-on-the-host
USER = ''  # user-name
PASSWORD = ''  # set database-password
HOST = 'xxx.xxx.xxx.xxx'  # set host IP address

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'set-secret-key-here'  # set-secret-key-here

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []

import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'mips.db'),
    }
}