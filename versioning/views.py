# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from versioning.models import Version

def index(request):
	all_versions = Version.objects.all().order_by('-created_on')
	return render_to_response('versioning/index.html', {'all_versions': all_versions}, context_instance=RequestContext(request))