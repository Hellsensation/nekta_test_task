# Generated by Django 4.2.6 on 2023-11-01 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nekta_requests', '0005_remove_request_user_requestmessage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestmessage',
            name='user',
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]