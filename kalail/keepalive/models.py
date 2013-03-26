from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class KeepAliveWebsite(models.Model):
	url = models.URLField()
	users = models.ManyToManyField(User)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.url