# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='Image_description',
            field=models.CharField(max_length=200),
        ),
    ]