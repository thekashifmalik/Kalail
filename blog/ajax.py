from django.core import serializers
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from blog.models import Post, Comment
from kalail.settings import DEBUG
from blog.tasks import send_comment_email

@dajaxice_register
def add_comment(request, post_id, new_comment):
	new_comment_dict = dict(item.split("=") for item in new_comment.split("&"))
	new_comment_captcha = new_comment_dict["new_comment_captcha"]
	new_comment_text = new_comment_dict["new_comment_text"]
	new_comment_author = new_comment_dict["new_comment_author"]
	# Process captcha.
	if new_comment_captcha.lower() == 'red':
		# Deal with empty comment.
		if new_comment_text != '':
			new_comment_post = Post.objects.get(id=post_id)
			new_comment = Comment(post=new_comment_post, text=new_comment_text, author=new_comment_author)
			new_comment.save()
			if not DEBUG:
				send_comment_email.delay()
	return simplejson.dumps({'text':new_comment.text, 'author':new_comment.author, 'created_on':new_comment.created_on.strftime("%m/%d/%Y %I:%M %p")})
	#return HttpResponseRedirect(reverse('blog.views.show_post', args=(post_id)))