# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from blog.models import Post, Comment


def index(request):
	all_posts = Post.objects.all().order_by('-created_on')
	return render_to_response('blog/index.html', {'all_posts': all_posts})

def show_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	comments = post.comment_set.all().order_by('created_on')
	return render_to_response('blog/show_post.html', {'post': post, 'comments': comments}, context_instance=RequestContext(request))

def add_comment(request, post_id):
	new_comment_text = request.POST['new_comment_text']
	new_comment_author = request.POST['new_comment_author']
	new_comment_post = Post.objects.get(id=post_id)
	new_comment = Comment(post=new_comment_post, text=new_comment_text, author=new_comment_author)
	new_comment.save()
	return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id)))

def about(request):
	return render_to_response('blog/about.html')

def contact(request):
	return render_to_response('blog/contact.html')
