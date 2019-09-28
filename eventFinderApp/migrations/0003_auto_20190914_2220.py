# Generated by Django 2.2 on 2019-09-14 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0002_event_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]