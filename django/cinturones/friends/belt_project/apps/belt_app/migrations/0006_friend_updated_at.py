# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-21 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0005_auto_20171221_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
