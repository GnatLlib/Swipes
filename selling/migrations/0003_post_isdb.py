# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0002_auto_20170219_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isDB',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]