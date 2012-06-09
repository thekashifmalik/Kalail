from django.test import TestCase
from versioning.models import Version
from django.core.urlresolvers import reverse


class versioning_testcase(TestCase):
	fixtures = ['versioning_testdata.json']

	def test_index_response_success(self):
		response = self.client.get(reverse('versioning.views.index'))
		self.assertEqual(response.status_code, 200)
	
	def test_index_content_success(self):
		test_version = Version.objects.latest('created_on')
		response = self.client.get(reverse('versioning.views.index'))
		self.assertContains(response, test_version.number)