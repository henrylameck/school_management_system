# Generated by Django 3.1 on 2020-12-11 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0005_auto_20201211_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exammarkentry',
            old_name='exam_mark_master',
            new_name='exam_master',
        ),
    ]
