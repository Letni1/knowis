# Generated by Django 2.0.13 on 2019-04-05 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, max_length=255, upload_to='images/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
