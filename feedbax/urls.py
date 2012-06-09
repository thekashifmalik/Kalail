from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feedbax.views',
	url(r'^$', 'index'),
	url(r'^setup/$', 'setup_feedback_system'),
	url(r'^show/(?P<feedbax_site>.+)/$', 'show_system_feedback'),
	url(r'^(?P<feedbax_site>.+)/$', 'send_feedback'),
	)