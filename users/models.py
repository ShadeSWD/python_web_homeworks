from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users_images/', null=True, blank=True, verbose_name='avatar')
    phone = models.CharField(unique=True, max_length=35, verbose_name='phone number')
    country = models.CharField(max_length=35, verbose_name='country')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = settings.DOMAIN_NAME + link
        subject = 'Подтверждение учетной записи'
        message = f'Для подтверждения перейдите по ссылке: {verification_link}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return now() >= self.expiration
