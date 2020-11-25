# Generated by Django 3.1 on 2020-11-25 05:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name of school')),
                ('code', models.CharField(max_length=100, verbose_name='School Code')),
                ('place', models.CharField(max_length=200, verbose_name='Place')),
                ('address', models.TextField()),
                ('postal_code', models.CharField(max_length=100, verbose_name='Postal Code')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_no_1', models.CharField(max_length=14)),
                ('phone_no_2', models.CharField(blank=True, max_length=14)),
                ('fax', models.CharField(blank=True, max_length=50)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('district', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('starting_date', models.DateField()),
                ('logo', models.ImageField(upload_to='logo')),
            ],
        ),
    ]
