# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-31 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_reviewer_app', '0007_auto_20171231_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(default=3),
        ),
    ]