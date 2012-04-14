from django.db import models

# Create your models here.
class Feedback(models.Model):
	content = models.TextField(max_length=64)
	user = models.CharField()
	system = 
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content

class TestSystem(models.Model):
	name = models.TextField()
	site = models.CharField(max_length=32)
	feedbax_site
	email = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name