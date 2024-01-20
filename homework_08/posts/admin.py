from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Post)
class FoodAdmin(admin.ModelAdmin):
    list_display = "id", "title", "text"
    list_display_links = "id", "title", "text"
