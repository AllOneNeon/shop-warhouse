# Generated by Django 3.2.6 on 2021-08-22 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_photo_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='product',
        ),
    ]