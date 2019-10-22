# Generated by Django 2.2.1 on 2019-06-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0011_auto_20190605_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='product_descr',
            field=models.FileField(upload_to='Mobile/description'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='product_image',
            field=models.ImageField(default=None, upload_to='Mobile/images'),
        ),
    ]
