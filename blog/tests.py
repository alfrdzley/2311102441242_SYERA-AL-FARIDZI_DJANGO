from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

class BlogViewsTest(TestCase):
    def setUp(self):
        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            subtitle='Test Subtitle',
            description='Test Description',
            image='images/test.jpg'
        )
        self.client = Client()

    def test_blog_list_view(self):
        # Test that the blog list view returns a 200 response
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        # Test that the post is in the context
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), 1)

    def test_blog_detail_view(self):
        # Test that the blog detail view returns a 200 response
        response = self.client.get(reverse('blog_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        # Test that the post is in the context
        self.assertIn('post', response.context)
        self.assertEqual(response.context['post'].title, 'Test Post')
