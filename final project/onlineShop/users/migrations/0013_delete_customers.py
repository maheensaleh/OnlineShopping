# Generated by Django 2.2.2 on 2019-07-15 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_customers_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customers',
        ),
    ]
