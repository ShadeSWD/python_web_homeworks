from django.db import models


class Category(models.Model):
    """Model of category of products"""
    category_name = models.CharField(max_length=150, verbose_name='category name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f"Product(pk={self.pk}, product_name={self.category_name!r})"


class Product(models.Model):
    """Model of product"""
    product_name = models.CharField(max_length=150, verbose_name='product name')
    description = models.TextField(verbose_name='description')
    preview = models.ImageField(verbose_name='preview', upload_to='products_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
