# Generated by Django 3.1 on 2020-12-05 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('classes', '0004_class_leaders'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.teacher'),
        ),
        migrations.AddField(
            model_name='classsyllabus',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher', verbose_name='H.O.D'),
        ),
    ]
