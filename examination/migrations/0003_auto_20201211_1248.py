# Generated by Django 3.1 on 2020-12-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_auto_20201211_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammarkentry',
            name='assignment_mark',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Assignment Marks'),
        ),
        migrations.AlterField(
            model_name='exammarkentry',
            name='practical_mark',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Practical Marks'),
        ),
        migrations.AlterField(
            model_name='exammarkentry',
            name='project_mark',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Project Marks'),
        ),
        migrations.AlterField(
            model_name='exammarkentry',
            name='theory_mark',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Theory Marks'),
        ),
    ]
