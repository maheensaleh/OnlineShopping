# Generated by Django 2.2b1 on 2019-06-15 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190614_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
    ]
