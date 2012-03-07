from django.test import TestCase
from blog.models import Post, Comment
import datetime

class blog_views_testcase(TestCase):
	fixtures = ['blog_views_testdata.json']

	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('all_posts' in response.context)
		self.assertEqual(response.context['all_posts'].get(id=2).title , 'Second Post!')

	def test_show_post(self):
		response = self.client.get('/post/')
		self.assertEqual(response.status_code, 404)

	def test_add_comment(self):
		post = Post.objects.get(pk=1)
		response = self.client.post('/1/add_comment/', {'new_comment_text': 'yo', 'new_comment_author': 'troll', 'new_comment_captcha': 'red' })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], 'http://testserver/1/')