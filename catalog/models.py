from django.db import models
from users.models import User


class Category(models.Model):
    """Model of category of products"""
    name = models.CharField(max_length=150, verbose_name='category name')
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name!r}"


class Product(models.Model):
    """Model of product"""
    name = models.CharField(max_length=150, verbose_name='product name')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(verbose_name='preview', upload_to='products_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    price = models.FloatField(verbose_name='price')
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name!r}"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='category')
    number = models.IntegerField(verbose_name='version number')
    name = models.CharField(max_length=200, verbose_name='version name')
    is_active = models.BooleanField(default=False, verbose_name='active')

    def __str__(self):
        return f"{self.name}"
