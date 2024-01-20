from django.test import TestCase
from posts.models import Category, Post


class CategoryTestCase(TestCase):
    def setUp(self):
        print('set up test')
        self.category = Category.objects.create(name='Новости')

    def tearDown(self):
        print('tear down test')

    def test_str_category(self):
        self.assertEqual(str(self.category), 'Новости')


class PostTestCase(TestCase):
    def test_str(self):
        category = Category.objects.create(name='Новости')
        post = Post.objects.create(category=category, title='Заголовок новости')
        self.assertEqual(str(post), 'Заголовок новости')