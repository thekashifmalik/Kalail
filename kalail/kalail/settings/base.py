# Django settings for kalail project.
import os

# Relative path settings
from unipath import Path
PROJECT_ROOT = Path(__file__).ancestor(3)

# Set various variables.
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = PROJECT_ROOT.child('media')

# Absolute path to the directory static files should be collected to using collectstatic.
STATIC_ROOT = ''

# Additional locations of static files - absolute paths
STATICFILES_DIRS = (
    PROJECT_ROOT.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

ROOT_URLCONF = 'kalail.urls'

# WSGI server for debug server.
WSGI_APPLICATION = 'kalail.wsgi.application'

# Templates location - absolute path
TEMPLATE_DIRS = (
    PROJECT_ROOT.child('templates'),
)


INSTALLED_APPS = (
    # Contrib
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django Suits needs to be before admin
    'suit',
    'django.contrib.admin',

    # Third party
    'south',
    'gunicorn',
    'social_auth',
    'django_extensions',
    'django_browserid',
    'storages',
    'djcelery',
    'suit_redactor',
    
    # Project
    'home',
    'blog',
    'versioning',
    'notes',
    'keepalive',
    # 'serviz',
)

# Set up Sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Celery settings
import djcelery
djcelery.setup_loader()

LOGIN_URL = '/sign_in/'
LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/login-error/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# Google Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django_browserid.context_processors.browserid",
)

# Celery settings
import djcelery
djcelery.setup_loader()

BROWSERID_CREATE_USER = True