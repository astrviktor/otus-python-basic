from django.http import HttpRequest
from django.shortcuts import render
from .models import Category, Post


def index_view(request):
    posts = (
        Post
        .objects
        .select_related("category")
        .all()
    )
    context = {
        "posts": posts,
    }
    return render(
        request,
        "posts/posts-list.html",
        context,
    )


def categories_with_posts(request: HttpRequest):
    context = {
        "categories": (
            Category
            .objects
            .prefetch_related("posts")
            .all()
        )
    }
    return render(
        request,
        "posts/categories-with-posts.html",
        context,
    )
