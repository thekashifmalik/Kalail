from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
	url(r'^$', 'index'),
	url(r'^about/$', 'about'),
	url(r'^contact/$', 'contact'),
	)