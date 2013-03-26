# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from keepalive.models import KeepAliveWebsite
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


@login_required
def index(request):
	if request.method == 'POST':
		website_urls = []
		website_urls.append(request.POST['website_1'])
		website_urls.append(request.POST['website_2'])
		website_urls.append(request.POST['website_3'])

		validate_url = URLValidator()
		valid_websites = []
		for website_url in website_urls:
			try:
				validate_url(website_url)
			except ValidationError:
				continue
			valid_websites.append(KeepAliveWebsite.objects.get_or_create(url = website_url)[0])

		request.user.keepalivewebsite_set = valid_websites

	websites_query = request.user.keepalivewebsite_set.all()[:3]
	fill_in = 3 - websites_query.count()
	websites = []
	for website in websites_query:
		websites.append(website.url)
	websites = websites + [""] * fill_in

	return render_to_response('keepalive/index.html', {"websites" : websites }, context_instance=RequestContext(request))
