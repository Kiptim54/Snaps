# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0007_auto_20180504_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snaps.Category'),
            preserve_default=False,
        ),
    ]
