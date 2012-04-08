# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from blog.models import Post, Comment
from django.views.decorators.cache import cache_page

@cache_page(60 * 30)
def index(request):
	all_posts = Post.objects.all().order_by('-created_on')
	return render_to_response('blog/index.html', {'all_posts': all_posts}, context_instance=RequestContext(request))

def show_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	comments = post.comment_set.all().order_by('created_on')
	return render_to_response('blog/show_post.html', {'post': post, 'comments': comments}, context_instance=RequestContext(request))

def add_comment(request, post_id):
	# Process captcha.
	new_comment_captcha = request.POST['new_comment_captcha']
	if new_comment_captcha.lower() == 'red':
		new_comment_text = request.POST['new_comment_text']
		# Deal with empty comment.
		if new_comment_text != '':
			new_comment_author = request.POST['new_comment_author']
			# Deal with empty author.
			if new_comment_author == '':
				new_comment_author = 'Anonymous'
			new_comment_post = Post.objects.get(id=post_id)
			new_comment = Comment(post=new_comment_post, text=new_comment_text, author=new_comment_author)
		
			new_comment.save()
	else:
		if request.session['just_failed_captcha'] == False:
			return HttpResponseRedirect(reverse('blog.views.index'))

		request.session['just_failed_captcha'] = False

	return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id)))
