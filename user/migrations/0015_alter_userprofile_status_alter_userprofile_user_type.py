# Generated by Django 5.0.3 on 2024-04-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STUDENT', 'Student'), ('STAFF', 'Staff'), ('EXAMCONTROLLER', 'Examcontroller')], max_length=20),
        ),
    ]
