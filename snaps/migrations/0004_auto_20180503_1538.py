# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0003_auto_20180503_1430'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categories',
            new_name='Category',
        ),
        migrations.RemoveField(
            model_name='location',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='categories',
        ),
        migrations.AddField(
            model_name='photo',
            name='image_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='snaps.Category'),
        ),
        migrations.AddField(
            model_name='photo',
            name='image_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snaps.Location'),
            preserve_default=False,
        ),
    ]
