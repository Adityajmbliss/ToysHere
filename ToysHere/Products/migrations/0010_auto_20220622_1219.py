# Generated by Django 3.0.14 on 2022-06-22 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_auto_20220621_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Category', verbose_name='Category'),
        ),
    ]
