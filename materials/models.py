from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='slug', null=True, blank=True)
    content = models.TextField(max_length=150, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='products/', verbose_name='картинка', null=True, blank=True)
    date_of_create = models.DateTimeField(verbose_name='Дата создания')
    publication_type = models.BooleanField(verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
