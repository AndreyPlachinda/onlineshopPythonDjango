# Generated by Django 2.1.3 on 2018-11-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181118_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара'),
        ),
    ]
