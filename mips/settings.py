"""Settings file """


import dbsettings_default as dbsettings

# for production use!
try:
    import dbsettings_production as dbsettings
except ImportError as ie:
    print "No production setting, load defaults"
    # pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = dbsettings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = dbsettings.ALLOWED_HOSTS


INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'mips',
    'django_nose',
    'coverage',
]

MIDDLEWARE_CLASSES = (
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = dbsettings.DATABASES

# # testing suit
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=mips',
    '--cover-inclusive',
    '--verbosity=2',
]