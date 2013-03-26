from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ModuleType(models.Model):
	name = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name


class Module(models.Model):
	type = models.ForeignKey(ModuleType)
	name = models.CharField(max_length=256)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.name

	def get_specific(self):
		t = self.type.name
		return getattr(self, t, None)


class Cache(Module):
	size = models.IntegerField(blank=True, null=True)
	cmd = models.CharField(max_length=512, blank=True)

	def __unicode__(self):
		return self.name


class ServiceType(models.Model):
	name = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name


class Service(models.Model):
	name = models.CharField(max_length=256)
	url = models.URLField(blank=True)
	type = models.ForeignKey(ServiceType)
	information = models.TextField(blank=True)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.name


class Server(models.Model):
	"""Server

	Server that contains modules.

	"""
	name = models.CharField(max_length=256)
	user = models.ForeignKey(User)
	modules = models.ManyToManyField(Module, blank=True, null=True)
	services = models.ManyToManyField(Service, blank=True, null=True)

	def __unicode__(self):
		return self.name