# Generated by Django 2.0.13 on 2019-04-09 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0005_useraccount_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='url',
        ),
    ]