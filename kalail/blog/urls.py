from django.conf.urls.defaults import patterns, include, url
from kalail.blog.feeds import LatestPostsFeed

urlpatterns = patterns('blog.views',
	url(r'^$', 'index'),
	url(r'^(?P<post_id>\d+)/$', 'show_post'),
	url(r'^(?P<post_id>\d+)/add_comment/$', 'add_comment'),
	url(r'^rss/$', LatestPostsFeed(), name='rss_feed'),
	)