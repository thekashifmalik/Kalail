from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('home.views',
	url(r'^$', 'index'),
	url(r'^software-engineer/$', 'software_engineer'),
	url(r'^film-director/$', 'film_director'),
	url(r'^sign_in/', 'sign_in'),
	url(r'^sign_out/$', 'sign_out'),
)