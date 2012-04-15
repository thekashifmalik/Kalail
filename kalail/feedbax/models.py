from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TestSystem(models.Model):
	name = models.CharField(max_length=64)
	site = models.URLField(max_length=200)
	feedbax_site = models.CharField(max_length=200)
	report_email = models.EmailField(max_length=32)
	users = models.ManyToManyField(User)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name


class Feedback(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User)
	system = models.ForeignKey(TestSystem)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content