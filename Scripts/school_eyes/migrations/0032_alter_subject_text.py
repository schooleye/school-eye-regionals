# Generated by Django 4.0.3 on 2022-05-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_eyes', '0031_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='text',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Maths', 'Maths')], max_length=20),
        ),
    ]
