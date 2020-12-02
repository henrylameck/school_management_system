# Generated by Django 3.1 on 2020-11-26 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_auto_20201126_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.academicsession', verbose_name='Select Academic Year')),
            ],
        ),
    ]