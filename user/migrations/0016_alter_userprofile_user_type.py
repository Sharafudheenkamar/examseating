# Generated by Django 5.0.3 on 2024-04-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('STAFF', 'Staff'), ('EXAMCONTROLLER', 'Examcontroller'), ('ADMIN', 'Admin')], max_length=20),
        ),
    ]