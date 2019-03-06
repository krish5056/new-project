# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-06 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstdoc', models.ImageField(default=False, upload_to='files')),
                ('seconddoc', models.ImageField(default=False, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phoneno', models.IntegerField()),
                ('address', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='documents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
    ]