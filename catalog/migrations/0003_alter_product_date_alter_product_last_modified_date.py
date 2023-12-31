# Generated by Django 4.2.2 on 2023-07-31 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_date_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата последнего изменения'),
        ),
    ]
