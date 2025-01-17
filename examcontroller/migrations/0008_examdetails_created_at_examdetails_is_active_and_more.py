# Generated by Django 5.0.3 on 2024-04-17 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examcontroller', '0007_remove_studentprofile_branchandsemester_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examdetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='examdetails',
            name='is_active',
            field=models.BooleanField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='examdetails',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='examhall',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='examhall',
            name='is_active',
            field=models.BooleanField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='examhall',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
