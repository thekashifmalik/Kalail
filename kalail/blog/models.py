from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=64)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	text = models.TextField()
	author = models.CharField(max_length=32)
	post = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text