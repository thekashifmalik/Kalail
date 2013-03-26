# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout


def index(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def software_engineer(request):
	return render_to_response('home/software_engineer.html',context_instance=RequestContext(request))

def film_director(request):
	return render_to_response('home/film_director.html',context_instance=RequestContext(request))

def sign_in(request):
	return render_to_response('home/sign_in.html',context_instance=RequestContext(request))

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home.views.index'))

