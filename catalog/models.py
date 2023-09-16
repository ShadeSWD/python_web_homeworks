from django.db import models


class Category(models.Model):
    """Model of category of products"""
    category_name = models.CharField(max_length=150, verbose_name='category name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f"Category(pk={self.pk}, category_name={self.category_name!r})"


class Product(models.Model):
    """Model of product"""
    product_name = models.CharField(max_length=150, verbose_name='product name')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(verbose_name='preview', upload_to='products_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    price = models.FloatField(verbose_name='price')
    created_at = models.DateTimeField(verbose_name='creation date')
    changed_at = models.DateTimeField(verbose_name='change date')

    def __str__(self):
        return f"Product(pk={self.pk}, product_name={self.product_name!r})"


class Contacts(models.Model):
    """Model of contacts"""
    country = models.CharField(max_length=150, verbose_name='country')
    itn = models.CharField(max_length=30, verbose_name='ITN')
    address = models.CharField(max_length=200, verbose_name='address')

    def __str__(self):
        return f"Contacts(pk={self.pk}, country={self.country!r})"


class Theme(models.Model):
    """Model of theme of posts"""
    theme_name = models.CharField(max_length=150, verbose_name='theme name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f"Theme(pk={self.pk}, theme_name={self.theme_name!r})"


class Post(models.Model):
    """Model of blog post"""
    post_name = models.CharField(max_length=150, verbose_name='post name')
    slug = models.CharField(max_length=20, verbose_name='slug', unique=True)
    containment = models.TextField(verbose_name='containment')
    preview = models.ImageField(verbose_name='preview', upload_to='products_images', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now_add=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='theme')
    views_count = models.PositiveIntegerField(verbose_name='views count', default=0)

    def __str__(self):
        return f"Post(pk={self.pk}, post_name={self.post_name!r})"
