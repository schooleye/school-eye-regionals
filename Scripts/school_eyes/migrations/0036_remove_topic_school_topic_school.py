# Generated by Django 4.0.3 on 2022-05-29 19:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_eyes', '0035_remove_profile_subjects_profile_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='school',
        ),
        migrations.AddField(
            model_name='topic',
            name='school',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
