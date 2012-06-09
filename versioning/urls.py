from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('versioning.views',
	url(r'^$', 'index'),
	)