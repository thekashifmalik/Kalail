# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext


def index(request):
	return render_to_response('main/index.html', context_instance=RequestContext(request))
	#return HttpResponseRedirect(reverse('blog.views.index'))

def	sign_in_needed(request):
	request.session['next'] = request.REQUEST.get('next', '')
	return render_to_response('main/sign_in_needed.html', context_instance=RequestContext(request))

def	sign_in(request):
	# request.session['next'] = request.REQUEST.get('next', '')
	return render_to_response('main/sign_in.html', context_instance=RequestContext(request))

def about(request):
	return render_to_response('main/about.html', context_instance=RequestContext(request))

def contact(request):
	return render_to_response('main/contact.html', context_instance=RequestContext(request))
