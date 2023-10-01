from django.db import models


class Post(models.Model):
    """Model of blog post"""
    name = models.CharField(max_length=150, verbose_name='post name')
    slug = models.CharField(max_length=20, verbose_name='slug', unique=True)
    containment = models.TextField(verbose_name='containment')
    preview = models.ImageField(verbose_name='preview', upload_to='products_images', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    views_count = models.PositiveIntegerField(verbose_name='views count', default=0)
    is_published = models.BooleanField(verbose_name='is published', default=True)

    def __str__(self):
        return f"{self.name!r}"

