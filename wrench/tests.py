from django.test.client import Client
from django.test.client import RequestFactory
from django.test import TestCase
from wrench.models import Project
from wrench.views import ListProjectView

class ProjectListViewTests(TestCase):

	def test_projects_in_the_context(self):

		client = Client()
		response = client.get('/')

		self.assertEquals(list(response.context['object_list']), [])

		Project.objects.create(name='test project')
		response = client.get('/')
		self.assertEquals(response.context['object_list'].count(), 1)

	def test_projects_in_the_context_request_factory(self):

		factory = RequestFactory()
		request = factory.get('/')

		response = ListProjectView.as_view()(request)

		self.assertEquals(list(response.context_data['object_list']), [])

		Project.objects.create(name='test project')
		response = ListProjectView.as_view()(request)
		self.assertEquals(response.context_data['object_list'].count(), 1)
