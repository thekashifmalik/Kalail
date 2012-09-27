# Django settings for kalail project.
import socket
import os
import django

DEBUG = TEMPLATE_DEBUG = False
STATIC_URL = 'https://s3.amazonaws.com/kalail_static/'

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__) + "/../../")

def relative_path(relative_root_path, target_file):
    return os.path.join(relative_root_path, target_file)

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Redis
import os
import urlparse

redis_url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost'))
BROKER_URL = os.environ.get('REDISTOGO_URL')
CELERY_REDIS_HOST = redis_url.hostname
CELERY_REDIS_PORT = redis_url.port
CELERY_REDIS_DB = 0

# Not Working with Django ORM
# CELERYBEAT_SCHEDULER = " djcelery.schedulers.DatabaseScheduler"

# Dajax
DAJAXICE_MEDIA_PREFIX ="dajaxice"
DAJAXICE_DEBUG = False

# Protected variables
SECRET_KEY = os.environ.get("SECRET_KEY")

# Amazon S3 setting
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

# Set up Cache
CACHES = {
 	'default': {
		'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
		'LOCATION': os.environ.get('MEMCACHIER_SERVERS', ''),
		'TIMEOUT': 500,
		'BINARY': True,
	}
}