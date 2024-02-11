from django.urls import reverse
from django.test import TestCase
from posts.models import Category


class PostsListViewTestCase(TestCase):

    def test_status_code(self):
        url = '/posts/list/'
        response = self.client.get(url)
        print('RESPONSE', response)
        print(type(response))
        self.assertEqual(response.status_code, 200)


class CategoryViewTestCase(TestCase):

    def setUp(self):
        self.url = '/posts/categories/'

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(self.url)
        context = response.context
        print(type(context))
        self.assertIn('categories', context)
        categories = context['categories']
        self.assertEqual(len(categories), 0)

        news = Category.objects.create(name='Новости')
        rumors = Category.objects.create(name='Слухи')

        response = self.client.get(self.url)
        context = response.context
        categories = context['categories']
        self.assertEqual(len(categories), 2)

    def test_content(self):
        response = self.client.get(self.url)
        content: bytes = response.content
        self.assertIn(b'Categories', content)
        self.assertIn('Categories', content.decode(encoding='utf-8'))
        self.assertContains(response, 'Categories', 2)


class PostsIndexViewTestCast(TestCase):

    def test_status_code(self):
        url = reverse('posts:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


