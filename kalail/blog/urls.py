from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'index'),
	url(r'^(?P<post_id>\d+)/$', 'show_post'),
	url(r'^(?P<post_id>\d+)/add_comment/$', 'add_comment'),
	url(r'^about/$', 'about'),
	url(r'^contact/$', 'contact'),
	)