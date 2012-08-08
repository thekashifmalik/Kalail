from celery.task import task, periodic_task
from django.core.mail import EmailMessage
from datetime import timedelta
import requests

@task
def send_comment_email():
	email_message = "A comment has been posted!"
	# Send email
	setup_email = EmailMessage('Comment Posted!', email_message, to=["kashif610@gmail.com"])
	setup_email.send()

@periodic_task(run_every = timedelta(seconds=60))
def send_request():
	r = requests.get('http://localhost:8000/')