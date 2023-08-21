from django.contrib.auth.models import AbstractUser
from django.db import models
from wheel.metadata import _

from catalog.models import NULLABLE, Product


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='mail')

    phone = models.CharField(max_length=25, verbose_name='phone', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='country', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    verification_key = models.CharField(max_length=20, default='Not_veryficate', verbose_name='Activate_key')

    user = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product', null=True, blank=True)

    is_active = models.BooleanField(default=False, verbose_name='Activate')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

