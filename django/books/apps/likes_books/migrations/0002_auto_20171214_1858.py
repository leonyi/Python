# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='uploaded_by_id',
            new_name='uploader',
        ),
    ]
