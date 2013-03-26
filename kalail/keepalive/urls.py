from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('keepalive.views',
	url(r'^$', 'index'),
	)