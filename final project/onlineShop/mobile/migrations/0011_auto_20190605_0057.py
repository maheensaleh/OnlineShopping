# Generated by Django 2.2.1 on 2019-06-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0010_auto_20190604_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='product_descr',
            field=models.FileField(upload_to='Mobile/Mobile/description'),
        ),
    ]
