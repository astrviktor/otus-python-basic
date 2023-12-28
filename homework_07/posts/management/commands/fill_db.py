from django.core.management.base import BaseCommand
from posts.models import Post, Category


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        posts = Post.objects.all()
        posts.delete()

        categories = Category.objects.all()
        categories.delete()

        news = Category.objects.create(name='Новости')
        news.save()
        rumors = Category.objects.create(name='Слухи')
        rumors.save()

        post1 = Post.objects.create(
            category=news,
            title='Новости',
            text=
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
            'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,'
            'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo'
            'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse'
            'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non'
            'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        )
        post1.save()

        post2 = Post.objects.create(
            category=rumors,
            title='Слухи',
            text=
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
            'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,'
            'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo'
            'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse'
            'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non'
            'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        )
        post2.save()
