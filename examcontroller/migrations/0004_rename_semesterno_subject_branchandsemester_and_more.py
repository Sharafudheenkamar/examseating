# Generated by Django 5.0.3 on 2024-04-08 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examcontroller', '0003_alter_studentprofile_auto_generate_registerno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='semesterno',
            new_name='branchandsemester',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='branch',
        ),
    ]
