from versioning.models import Version
from django.contrib import admin

class VersionAdmin(admin.ModelAdmin):
	fields = ['number', 'features']
	list_display = ('number', 'features', 'created_on')
	search_fields = ['number', 'features']

admin.site.register(Version, VersionAdmin)