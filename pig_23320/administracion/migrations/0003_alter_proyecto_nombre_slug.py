# Generated by Django 3.2 on 2023-05-29 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='nombre_slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Nombre Slug'),
        ),
    ]
