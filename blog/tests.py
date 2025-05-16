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
        response = self.client.get(reverse('blog_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        # Test that the post is in the context
        self.assertIn('post', response.context)
        self.assertEqual(response.context['post'].title, 'Test Post')


from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BlogSignupViewTests(TestCase):
    def successful_signup_creates_user(self):
        response = self.client.post(reverse('blog_signup'), {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def signup_with_missing_fields_returns_error(self):
        response = self.client.post(reverse('blog_signup'), {
            'username': '',
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 200)  # Stays on signup page
        self.assertFalse(User.objects.filter(email='testuser@example.com').exists())

    def signup_with_existing_username_returns_error(self):
        User.objects.create_user(username='testuser', password='testpassword123', email='testuser@example.com')
        response = self.client.post(reverse('blog_signup'), {
            'username': 'testuser',
            'password': 'newpassword123',
            'email': 'newemail@example.com'
        })
        self.assertEqual(response.status_code, 200)  # Stays on signup page
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)
