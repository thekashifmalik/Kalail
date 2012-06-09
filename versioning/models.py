from django.db import models

# Create your models here.
class Version(models.Model):
	number = models.CharField(max_length=9)
	features = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.number