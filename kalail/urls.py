from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kalail import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Dajax
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

urlpatterns = patterns('',
	url(r'^blog/', include('blog.urls')),
	url(r'^versions/', include('versioning.urls')),
    url(r'^notes/', include('notes.urls')),
    # Examples:
    # url(r'^$', 'kalail.views.home', name='home'),
    # url(r'^kalail/', include('kalail.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    url(r'', include('social_auth.urls')),
    url(r'^', include('kalail.main.urls')),
    #url(r'^$', redirect_to, {'url': '/blog/'}),
)

urlpatterns += staticfiles_urlpatterns()