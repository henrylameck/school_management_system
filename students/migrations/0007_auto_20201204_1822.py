# Generated by Django 3.1 on 2020-12-04 15:22

from django.db import migrations, models
import django.db.models.deletion
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20201204_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentadmission',
            name='roll',
            field=models.CharField(default=students.models.random_string, max_length=50),
        ),
        migrations.AlterField(
            model_name='studentadmission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.studentregistration', unique=True),
        ),
    ]
