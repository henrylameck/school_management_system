# Generated by Django 3.1 on 2020-12-11 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination', '0003_auto_20201211_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammaster',
            name='last_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
