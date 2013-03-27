from blog.models import Post
from django.forms import ModelForm
from django.contrib import admin
from suit_redactor.widgets import RedactorWidget

class PostForm(ModelForm):
	class Meta:
		widgets = {
			'body': RedactorWidget(editor_options={'lang': 'en'})
		}

class PostAdmin(admin.ModelAdmin):
	form = PostForm
	list_display = ('title', 'body', 'created_on')
	fieldsets = [
		('Title', {'fields': ('title',)}),
		('Body', {'classes': ('full-width',), 'fields': ('body',)})
	]



admin.site.register(Post, PostAdmin)