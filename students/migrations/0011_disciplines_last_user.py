# Generated by Django 3.1 on 2020-12-07 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0010_auto_20201204_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplines',
            name='last_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discipline_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]