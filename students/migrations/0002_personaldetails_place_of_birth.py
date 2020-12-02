# Generated by Django 3.1 on 2020-12-02 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='place_of_birth',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Place of Birth'),
            preserve_default=False,
        ),
    ]