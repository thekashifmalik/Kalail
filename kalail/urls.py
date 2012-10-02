from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kalail import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^blog/', include('blog.urls')),
	url(r'^versions/', include('versioning.urls')),
    url(r'^notes/', include('notes.urls')),
    url(r'^keep-alive/', include('keepalive.urls')),
    url(r'^browserid/', include('django_browserid.urls')),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('kalail.main.urls')),
)

urlpatterns += staticfiles_urlpatterns()