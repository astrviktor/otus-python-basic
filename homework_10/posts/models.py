from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self):
        return self.title

