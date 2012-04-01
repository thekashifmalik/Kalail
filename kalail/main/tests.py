from django.test import TestCase
from django.core.urlresolvers import reverse


class main_testcase(TestCase):

	def test_about_response_success(self):
		response = self.client.get(reverse('main.views.about'))
		self.assertEqual(response.status_code, 200)
	
	def test_about_content_success(self):
		response = self.client.get(reverse('main.views.about'))
		self.assertContains(response, 'About')

	def test_contact_response_success(self):
		response = self.client.get(reverse('main.views.contact'))
		self.assertEqual(response.status_code, 200)
	
	def test_contact_content_success(self):
		response = self.client.get(reverse('main.views.contact'))
		self.assertContains(response, 'Contact')