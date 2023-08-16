from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    nomination = models.CharField(max_length=30, verbose_name='наименование', unique=True, **NULLABLE)
    description = models.TextField(verbose_name='Описание', unique=True, **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='картинка', null=True, blank=True)
    category = models.CharField(max_length=30)
    price = models.IntegerField(verbose_name='цена')
    date = models.DateTimeField(verbose_name='дата', null=True, blank=True)
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения', null=True, blank=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='creator')

    def __str__(self):
        return f"{self.nomination} {self.description}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    nomination = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.nomination}\n{self.description}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    version_number = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=50, verbose_name='название версии')
    version_control = models.BooleanField(verbose_name='признак версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f"{self.name_version} {self.version_number}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
