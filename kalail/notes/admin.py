from notes.models import Notepad
from django.contrib import admin

class NotepadAdmin(admin.ModelAdmin):
	fields = ['body']
	list_display = ('user', 'body', 'created_on')
	search_fields = ['user', 'body']

admin.site.register(Notepad, NotepadAdmin)