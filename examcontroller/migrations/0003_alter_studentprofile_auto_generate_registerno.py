# Generated by Django 5.0.3 on 2024-04-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examcontroller', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='auto_generate_registerno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]