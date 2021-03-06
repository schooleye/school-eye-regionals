# Generated by Django 4.0.3 on 2022-05-22 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_eyes', '0018_alter_coverage_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coverage',
            old_name='coverage',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='coverage',
            name='topic',
        ),
        migrations.AddField(
            model_name='topic',
            name='coverage',
            field=models.ForeignKey(blank='TRUE', null='TRUE', on_delete=django.db.models.deletion.CASCADE, to='school_eyes.coverage'),
            preserve_default='TRUE',
        ),
    ]
