# Generated by Django 5.0.3 on 2024-04-17 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('EXAMCONTROLLER', 'Examcontroller'), ('STUDENT', 'Student'), ('STAFF', 'Staff'), ('ADMIN', 'Admin')], max_length=20),
        ),
    ]
