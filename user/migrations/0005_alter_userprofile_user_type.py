# Generated by Django 5.0.3 on 2024-04-08 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('EXAMCONTROLLER', 'Examcontroller'), ('STAFF', 'Staff'), ('ADMIN', 'Admin')], max_length=20),
        ),
    ]
