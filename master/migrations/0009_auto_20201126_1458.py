# Generated by Django 3.1 on 2020-11-26 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_academicyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicyear',
            name='year',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='master.academicsession', verbose_name='Select Academic Year'),
        ),
    ]
