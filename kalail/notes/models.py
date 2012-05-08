from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notepad(models.Model):
	body = models.TextField(blank=True)
	author = models.ForeignKey(User)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "Notepad of " + self.author.first_name