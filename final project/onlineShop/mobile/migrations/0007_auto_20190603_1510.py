# Generated by Django 2.2.1 on 2019-06-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0006_auto_20190603_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samsung',
            name='p_descr',
        ),
        migrations.RemoveField(
            model_name='samsung',
            name='p_price',
        ),
        migrations.RemoveField(
            model_name='samsung',
            name='p_quantity',
        ),
        migrations.RemoveField(
            model_name='samsung',
            name='product_name',
        ),
        migrations.AddField(
            model_name='samsung',
            name='product_descr',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='samsung',
            name='product_model',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='samsung',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='samsung',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
