# Django settings for kalail project.
import socket
import os
import django

# app_env = os.environ["KALAIL_ENV"]

# if app_env == "production":

# else if app_env == "development":

# else:


if socket.gethostname() == 'Kalail-PC':
    DEBUG = TEMPLATE_DEBUG = False
    STATIC_URL = 'https://s3.amazonaws.com/kalail_static/'
else:
    DEBUG = TEMPLATE_DEBUG = False
    STATIC_URL = 'https://s3.amazonaws.com/kalail_static/'


# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__) + "/../../")

def relative_path(relative_root_path, target_file):
    return os.path.join(relative_root_path, target_file)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if socket.gethostname() == 'Kalail-PC':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'kalail_db',                      # Or path to database file if using sqlite3.
            'USER': 'kalail_db_user',                      # Not used with sqlite3.
            'PASSWORD': 'kalail_db_password',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = relative_path(SITE_ROOT, 'static')
STATIC_ROOT = '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    relative_path(SITE_ROOT, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dhejs&r+c7l!!(7r79zd_je1&e549&w0y72f$+ljj*n107#xew'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'kalail.urls'

TEMPLATE_DIRS = (
    relative_path(SITE_ROOT, 'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'kalail.main',
    'blog',
    'versioning',
    'south',
    'gunicorn',
    'storages',
    'debug_toolbar',
    'social_auth',
    'django_extensions',
    'notes',
    'djcelery',
    'dajaxice',
    'keepalive',
    'raven.contrib.django',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

# Amazon S3 setting
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAI7EOYMFRURZPCUKA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'kalail_static'
AWS_TEMP_STORAGE_BUCKET_NAME = 'kalail_temp'

# Django debug toolbar
INTERNAL_IPS = (
    '127.0.0.1',
    )

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Set up Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

# Set up Sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


# Email Setup
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kalail@kalail.com'
EMAIL_HOST_PASSWORD = 'batmanbatman'
EMAIL_PORT = 587

# Google Authentication
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

GOOGLE_DISPLAY_NAME = 'Kalail.com'

LOGIN_URL = '/sign_in_needed/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

# Twitter settings
TWITTER_USERNAME = "kashif610"
TWITTER_CACHE_TIMEOUT = 60 * 5

# Celery settings
import djcelery
djcelery.setup_loader()

# Redis
import os
import urlparse

CELERY_RESULT_BACKEND = "redis"
if socket.gethostname() == 'Kalail-PC':
    BROKER_URL = "redis://localhost:6379/0"
    CELERY_REDIS_HOST = "localhost"
    CELERY_REDIS_PORT = 6379
    CELERY_REDIS_DB = 0
else:
    redis_url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost'))
    BROKER_URL = os.environ.get('REDISTOGO_URL')
    CELERY_REDIS_HOST = redis_url.hostname
    CELERY_REDIS_PORT = redis_url.port
    CELERY_REDIS_DB = 0

# Not Working with Django ORM
# CELERYBEAT_SCHEDULER = " djcelery.schedulers.DatabaseScheduler"

# Dajax
DAJAXICE_MEDIA_PREFIX ="dajaxice"
if socket.gethostname() == 'Kalail-PC':
    DAJAXICE_DEBUG = True
else:
    DAJAXICE_DEBUG = False