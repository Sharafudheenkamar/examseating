# Generated by Django 5.0.3 on 2024-04-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examcontroller', '0014_examstudymaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatingarrangement',
            name='exam_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seatingarrangement',
            name='exam_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
