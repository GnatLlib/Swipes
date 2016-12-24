# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
            preserve_default=False,
        ),
    ]
