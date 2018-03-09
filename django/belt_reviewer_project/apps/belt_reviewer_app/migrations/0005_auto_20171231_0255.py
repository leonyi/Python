# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-31 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_reviewer_app', '0004_auto_20171231_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploader',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='book_uploads', to='belt_reviewer_app.User'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='belt_reviewer_app.User'),
        ),
    ]
