# Generated by Django 5.0.3 on 2024-04-08 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('exam_time', models.TimeField(blank=True, null=True)),
                ('no_of_students', models.CharField(blank=True, max_length=100, null=True)),
                ('duration_hours', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Studentprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerno', models.CharField(blank=True, max_length=30, null=True)),
                ('auto_generate_registerno', models.CharField(blank=True, max_length=455, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(blank=True, max_length=100, null=True)),
                ('subjectcode', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('autogeneratesubjectcode', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semesterno', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examcontroller.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Staffprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, max_length=30, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffsubject', to='examcontroller.semester')),
            ],
        ),
    ]