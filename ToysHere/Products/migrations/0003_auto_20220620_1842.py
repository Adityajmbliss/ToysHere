# Generated by Django 3.0.14 on 2022-06-20 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20220620_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]