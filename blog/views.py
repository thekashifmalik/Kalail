# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from blog.models import Post, Comment
from django.views.decorators.cache import cache_page
from blog.tasks import send_comment_email
from kalail.settings import DEBUG
from blog.tasks import send_comment_email
import json

@cache_page(1 * 60)
def index(request):
	all_posts = Post.objects.all().order_by('-created_on')
	return render_to_response('blog/index.html', {'all_posts': all_posts}, context_instance=RequestContext(request))

def redirect_to_slug_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id, post.slug)))

@cache_page(30)
def show_post(request, post_id, post_slug):
	post = get_object_or_404(Post, id=post_id)
	if post_slug != post.slug:
		 return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id, post.slug)))
	comments = post.comment_set.all().order_by('created_on')
	return render_to_response('blog/show_post.html', {'post': post, 'comments': comments}, context_instance=RequestContext(request))
