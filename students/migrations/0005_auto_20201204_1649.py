# Generated by Django 3.1 on 2020-12-04 13:49

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20201204_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentadmission',
            name='reg_no',
            field=models.CharField(default=1, max_length=100, verbose_name='Registration No:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentadmission',
            name='roll',
            field=models.IntegerField(default=students.models.random_string),
        ),
    ]
