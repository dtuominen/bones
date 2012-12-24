# Django settings for myproject project.
import sys
from os.path import abspath, basename, dirname, join, normpath

##### Path config #####
# Assumes settings file is located in /settings/
# DJANGO_ROOT would return /myproject/myproject
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

SITE_NAME = basename(DJANGO_ROOT)

# absolute path to the top level of the project
SITE_ROOT = dirname(DJANGO_ROOT)

# add the top level path the the system python path
sys.path.append(SITE_ROOT)

# allows for a structure where apps are kept in myproject/apps/myapp
sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
##### End path config #####

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': normpath(join(DJANGO_ROOT, 'task.db')),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# 'who cares' settings
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

##### MEDIA FILE CONFIG #####
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
MEDIA_URL = '/media/'

#### STATIC FILE CONFIG #####
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'media'))
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# dump static files into myproject/myproject/staticdump for collection
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'staticdump')),
)
##### END STATIC CONFIG #####

##### TEMPLATE CONFIG #####
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    # keep your templates in myproject/myproject/templates
    normpath(join(DJANGO_ROOT, 'templates')),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)

##### URL/WSGI CONF #####
ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'



INSTALLED_APPS = (
    # My apps
    'basicapp',

    # 3rd party apps
    'south',
    'django_extensions',
    'debug_toolbar',

    # Built-in apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

SECRET_KEY = 'vm@nx(dy2u=z&amp;tf18y)6em)ee38fmd@z463g$53tt5d4@a&amp;uqa'
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
