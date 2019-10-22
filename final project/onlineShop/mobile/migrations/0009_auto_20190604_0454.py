# Generated by Django 2.2.1 on 2019-06-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0008_samsung_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_descr', models.CharField(default='', max_length=200)),
                ('product_price', models.IntegerField(default=0)),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_brand', models.CharField(default='', max_length=40)),
                ('product_model', models.CharField(default='', max_length=50)),
                ('product_image', models.ImageField(default=None, upload_to='Mobile/images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Samsung',
        ),
    ]
