# Generated by Django 3.1 on 2020-12-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20201204_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentadmission',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='students.studentregistration'),
        ),
    ]
