# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugrajapp', '0002_auto_20161004_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='newmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wholestring', models.CharField(max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
