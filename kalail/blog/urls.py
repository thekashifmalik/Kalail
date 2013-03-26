from django.conf.urls.defaults import patterns, url
from blog.feeds import LatestPostsFeed

urlpatterns = patterns('blog.views',
	url(r'^$', 'index'),
	url(r'^(?P<post_id>\d+)/$', 'redirect_to_slug_post'),
	url(r'^(?P<post_id>\d+)/(?P<post_slug>[-\w]+)/$', 'show_post'),
	url(r'^rss/$', LatestPostsFeed(), name='rss_feed'),
	)