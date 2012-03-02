from blog.models import Post, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'body']
	list_display = ('title', 'body', 'created_on')
	search_fields = ['title', 'body']

class CommentAdmin(admin.ModelAdmin):
	fields = ['post', 'text', 'author']
	list_display = ('text', 'author', 'created_on', 'post')
	search_fields = ['text', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)