from django.test import TestCase
from blog.models import Post
from django.core.urlresolvers import reverse

class blog_testcase(TestCase):
	fixtures = ['blog_testdata.json']

	def test_index_response_success(self):
		response = self.client.get(reverse('blog.views.index'))
		self.assertEqual(response.status_code, 200)

	def test_index_content_success(self):
		#test_post = Post.objects.latest('created_on')
		test_post = Post.objects.get(pk=1)
		response = self.client.get(reverse('blog.views.index'))
		self.assertContains(response, test_post.title)
	
	def test_show_post_response_success(self):
		test_post = Post.objects.latest('created_on')
		response = self.client.get(reverse('blog.views.show_post', args=(str(test_post.pk))))
		self.assertEqual(response.status_code, 200)

	def test_show_post_content_success(self):
		#test_post = Post.objects.latest('created_on')
		test_post = Post.objects.get(pk=1)		
		response = self.client.get(reverse('blog.views.show_post', args=(str(test_post.pk))))
		self.assertContains(response, test_post.title)

