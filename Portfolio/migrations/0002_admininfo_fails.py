# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='fails',
            field=models.IntegerField(default=0),
        ),
    ]
