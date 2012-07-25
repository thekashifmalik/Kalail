from blog.models import Post, Comment
from django.contrib import admin
from kalail.settings import STATIC_URL

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'body']
	list_display = ('title', 'body', 'created_on')
	search_fields = ['title', 'body']

class CommentAdmin(admin.ModelAdmin):
	fields = ['post', 'text', 'user']
	list_display = ('text', 'user', 'created_on', 'post')
	search_fields = ['text', 'user']

class CommonMedia:
	js = (
    	'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    	STATIC_URL + 'admin/js/editor.js',
  	)
  	css = {
    	'all': (STATIC_URL + 'admin/css/editor.css',),
	}

admin.site.register(Post, PostAdmin, Media = CommonMedia)
admin.site.register(Comment, CommentAdmin)