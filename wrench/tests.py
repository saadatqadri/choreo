from django.test.client import Client
from django.test.client import RequestFactory
from django.test import TestCase
from wrench.models import Project
from wrench.views import ListProjectView

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


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


class ProjectListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ProjectListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ProjectListIntegrationTests, cls).tearDownClass()

    def test_project_listed(self):

        # create a test project
        Project.objects.create(name='Test Project')

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.project')[0].text,
            'Test Project'
        )

    def test_add_project(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/projects/new'))
        self.selenium.find_element_by_id('id_name').send_keys('test project')
        self.selenium.find_element_by_id('save_project').click()

        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.project')[0].text,
            'Project: test project'
        )
