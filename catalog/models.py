from django.db import models


class Category(models.Model):
    """Model of category of products"""
    name = models.CharField(max_length=150, verbose_name='category name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f"Category(pk={self.pk}, category_name={self.name!r})"


class Product(models.Model):
    """Model of product"""
    name = models.CharField(max_length=150, verbose_name='product name')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(verbose_name='preview', upload_to='products_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    price = models.FloatField(verbose_name='price')
    created_at = models.DateTimeField(verbose_name='creation date')
    changed_at = models.DateTimeField(verbose_name='change date')

    def __str__(self):
        return f"Product(pk={self.pk}, product_name={self.name!r})"
