# Generated by Django 3.1 on 2020-12-07 11:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_auto_20201207_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformreceive',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'Please select'), ('male', 'Male'), ('Female', 'Female')], max_length=12),
        ),
    ]
