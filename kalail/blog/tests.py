from django.test import TestCase
from blog.models import Post, Comment
from django.core.urlresolvers import reverse
import datetime

class views_testcase(TestCase):
	fixtures = ['blog_views_testdata.json']

	def test_index_success(self):
		response = self.client.get(reverse('blog.views.index'))
		self.assertEqual(response.status_code, 200)
	
	def test_show_post_success(self):
		response = self.client.get(reverse('blog.views.show_post', args=('1')))
		self.assertEqual(response.status_code, 200)
		test_post = Post.objects.get(pk=1)
		self.assertContains(response, test_post.title)
		self.assertContains(response, test_post.body)

	def test_show_post_fail(self):
		response = self.client.get('/-1/')
		self.assertEqual(response.status_code, 404)

	def test_add_comment_success(self):
		test_comment = Comment(text='This is a test!', author='Tester')
		response = self.client.post('/blog/1/add_comment/', {'new_comment_text': test_comment.text, 'new_comment_author': test_comment.author, 'new_comment_captcha': 'red' })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], 'http://testserver/blog/1/')
		post = Post.objects.get(pk=1)
		self.assertEqual(post.comment_set.latest('created_on').text, test_comment.text)
		self.assertEqual(post.comment_set.latest('created_on').author, test_comment.author)

	def test_add_comment_fail(self):
		test_comment = Comment(text='This is a test!', author='Tester')
		response = self.client.post('/blog/1/add_comment/', {'new_comment_text': test_comment.text, 'new_comment_author': test_comment.author, 'new_comment_captcha': 'blue' })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], 'http://testserver/blog/1/')
		post = Post.objects.get(pk=1)
		self.assertNotEqual(post.comment_set.latest('created_on').text, test_comment.text)
		self.assertNotEqual(post.comment_set.latest('created_on').author, test_comment.author)