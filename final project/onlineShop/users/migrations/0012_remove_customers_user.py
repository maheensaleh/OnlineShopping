# Generated by Django 2.2b1 on 2019-06-21 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190619_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='user',
        ),
    ]
