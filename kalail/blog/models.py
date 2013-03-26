from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
	title = models.CharField(max_length=64)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	@property
	def slug(self):
		return slugify(self.title)


	def __unicode__(self):
		return self.title