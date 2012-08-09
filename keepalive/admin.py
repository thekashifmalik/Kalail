from keepalive.models import KeepAliveWebsite
from django.contrib import admin

class KeepAliveWebsiteAdmin(admin.ModelAdmin):
	fields = ['url', 'users']
	list_display = ('url', 'created_on')
	search_fields = ['url', 'users']

admin.site.register(KeepAliveWebsite, KeepAliveWebsiteAdmin)