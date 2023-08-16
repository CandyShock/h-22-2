# Generated by Django 4.2.2 on 2023-08-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(unique=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nomination',
            field=models.CharField(max_length=30, unique=True, verbose_name='наименование'),
        ),
    ]
