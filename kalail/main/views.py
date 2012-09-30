# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from blog.models import Post
from kalail.settings import TWITTER_USERNAME
from django.views.decorators.cache import cache_page


# @cache_page(1 * 60)
def index(request):
	return render_to_response('main/index.html',context_instance=RequestContext(request))

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('kalail.main.views.index'))

