# Generated by Django 4.2.2 on 2023-08-16 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_creator'),
        ('users', '0005_user_verification_key_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Activate'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_key',
            field=models.CharField(default='Not_veryficate', max_length=20, verbose_name='Activate_key'),
        ),
    ]
