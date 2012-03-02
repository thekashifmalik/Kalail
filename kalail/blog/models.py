from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=64, blank=False)
	body = models.TextField(blank=False)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	text = models.TextField(blank=False)
	author = models.CharField(max_length=32, blank=False)
	post = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text