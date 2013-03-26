from django.test import TestCase
from notes.models import Notepad
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.models import User


class notes_testcase(TestCase):

	def setUp(self):
		User.objects.create_user('test_user_name', 'test_user@email.com', 'test_user_password')

	def test_signed_out_index_response_success(self):
		response = self.client.get(reverse('notes.views.index'))
		self.assertEqual(response.status_code, 302)

	def test_signed_in_index_response_success(self):
		self.client.login(username='test_user_name', password='test_user_password')
		response = self.client.get(reverse('notes.views.index'))
		self.assertEqual(response.status_code, 200)

	def test_signed_in_index_creates_notepad_success(self):
		self.client.login(username='test_user_name', password='test_user_password')
		response = self.client.get(reverse('notes.views.index'))
		user = User.objects.get(id = self.client.session['_auth_user_id'])
		self.assertIsInstance(user.notepad, Notepad)

	def test_signed_in_index_shows_notepad_success(self):
		self.client.login(username='test_user_name', password='test_user_password')
		self.client.get(reverse('notes.views.index'))
		user = User.objects.get(id = self.client.session['_auth_user_id'])
		user.notepad.body = "Test Test Test"
		user.notepad.save()
		response = self.client.get(reverse('notes.views.index'))
		self.assertContains(response, user.notepad.body)