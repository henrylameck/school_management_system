# Generated by Django 3.1 on 2020-12-04 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_auto_20201126_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='website',
        ),
    ]
