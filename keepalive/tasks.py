from celery.task import task, periodic_task
from keepalive.models import KeepAliveWebsite
import requests
from datetime import timedelta
from requests.exceptions import RequestException

@periodic_task(run_every = timedelta(seconds=60))
def send_requests():
	websites = KeepAliveWebsite.objects.all()
	for website in websites:
		try:
			requests.get(website.url, timeout=30)
		except RequestException:
			continue

@periodic_task(run_every = timedelta(hours=1))
def remove_unused_websites():
	websites = KeepAliveWebsite.objects.all()
	for website in websites:
		if website.users.all() == []:
			website.delete()