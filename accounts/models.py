from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model


User = get_user_model()

# class User(AbstractUser):
#     photo = models.ImageField(upload_to='users', null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)



class BlackListedIPAddresses(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name_plural = 'Black Listed IP Addresses'
        verbose_name = 'Black Listed IP Address'