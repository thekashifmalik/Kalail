from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Post

class LatestPostsFeed(Feed):
	title = "Kalail"
	link = '/'
	description = "Latest blog posts on Kalail.com"

	def items(self):
		return Post.objects.all().order_by('-created_on')[:7]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body

	def item_link(self, item):
		return reverse('blog.views.show_post', args=(str(item.id)))