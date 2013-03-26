import os

# Debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Amazon S3 setting
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'kalail_dev'

DEFAULT_FILE_STORAGE = 'helpers.storages.MediaS3Storage'
STATICFILES_STORAGE = 'helpers.storages.StaticS3Storage'

# URL prefix for files.
STATIC_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/static/'
MEDIA_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/media/'

# RabbitMQ
BROKER_URL = os.environ.get('CLOUDAMQP_URL')
BROKER_POOL_LIMIT = 1

# Memcachier
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

# Cache settings
CACHES = {
 	'default': {
		'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
		'LOCATION': os.environ.get('MEMCACHIER_SERVERS', ''),
		'TIMEOUT': 500,
		'BINARY': True,
	}
}

SECRET_KEY = os.environ.get('SECRET_KEY')

# Browser ID settings
SITE_URL = 'http://kalail-dev.herokuapp.com'