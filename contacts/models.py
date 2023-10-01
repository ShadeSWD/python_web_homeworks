from django.db import models


class Contacts(models.Model):
    """Model of contacts"""
    country = models.CharField(max_length=150, verbose_name='country')
    itn = models.CharField(max_length=30, verbose_name='ITN')
    address = models.CharField(max_length=200, verbose_name='address')

    def __str__(self):
        return f"Contacts(pk={self.pk}, country={self.country!r})"
    