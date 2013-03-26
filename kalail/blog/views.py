# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from blog.models import Post


def index(request):
	all_posts = Post.objects.all().order_by('-created_on')
	return render_to_response('blog/index.html', {'all_posts': all_posts}, context_instance=RequestContext(request))

def redirect_to_slug_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id, post.slug)))

def show_post(request, post_id, post_slug):
	post = get_object_or_404(Post, id=post_id)
	if post_slug != post.slug:
		 return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id, post.slug)))
	return render_to_response('blog/show_post.html', {'post': post}, context_instance=RequestContext(request))
