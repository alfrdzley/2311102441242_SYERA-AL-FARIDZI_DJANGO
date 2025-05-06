from django.test import TestCase, Client
from django.urls import reverse
from .models import Project

class ProjectViewsTest(TestCase):
    def setUp(self):
        # Create a test project
        self.project = Project.objects.create(
            title='Test Project',
            subtitle='Test Subtitle',
            description='Test Description',
            image='images/test.jpg',
            client='Test Client',
            year='2024',
            services='Test Services',
            project_type='Test Type'
        )
        self.client = Client()

    def test_projects_list_view(self):
        # Test that the projects list view returns a 200 response
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        # Test that the project is in the context
        self.assertIn('projects', response.context)
        self.assertEqual(len(response.context['projects']), 1)

    def test_project_detail_view(self):
        # Test that the project detail view returns a 200 response
        response = self.client.get(reverse('project_detail', args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        # Test that the project is in the context
        self.assertIn('project', response.context)
        self.assertEqual(response.context['project'].title, 'Test Project')
