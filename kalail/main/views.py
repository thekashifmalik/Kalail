# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from blog.models import Post
from kalail.settings import TWITTER_USERNAME
import twitter

@cache_page(1 * 60)
def index(request):
	# recent_blogposts = Post.objects.all().order_by('-created_on')[:3]
	# try:
	# 	recent_tweets = twitter.Api().GetUserTimeline(TWITTER_USERNAME)[:5]
	# except Exception:
	# 	recent_tweets = None
	return render_to_response('main/index.html',context_instance=RequestContext(request))
	#return HttpResponseRedirect(reverse('blog.views.index'))

def	sign_in_needed(request):
	request.session['next'] = request.REQUEST.get('next', '')
	return render_to_response('main/sign_in_needed.html', context_instance=RequestContext(request))

def	sign_in(request):
	# request.session['next'] = request.REQUEST.get('next', '')
	return render_to_response('main/sign_in.html', context_instance=RequestContext(request))

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('kalail.main.views.index'))

