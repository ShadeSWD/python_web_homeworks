from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users_images/', null=True, blank=True, verbose_name='avatar')
    phone = models.CharField(unique=True, max_length=35, verbose_name='phone number')
    country = models.CharField(max_length=35, verbose_name='country')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
