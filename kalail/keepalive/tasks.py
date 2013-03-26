from celery.task import task, periodic_task
from keepalive.models import KeepAliveWebsite
import requests
from datetime import timedelta
from requests.exceptions import RequestException

@periodic_task(run_every = timedelta(minutes=30))
def send_requests():
	websites = KeepAliveWebsite.objects.all()
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}
	for website in websites:
		try:
			requests.get(website.url, prefetch=True, headers=headers, timeout=30)
		except RequestException:
			pass

@periodic_task(run_every = timedelta(minutes=10))
def remove_unused_websites():
	websites = KeepAliveWebsite.objects.all()
	for website in websites:
		if not website.users.all().exists():
			website.delete()