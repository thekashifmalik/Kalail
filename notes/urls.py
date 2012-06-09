from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('notes.views',
	url(r'^$', 'index'),
	)