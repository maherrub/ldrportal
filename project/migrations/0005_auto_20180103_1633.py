# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-03 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20180101_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ldrscheduledactivity',
            old_name='avtivityEditedOn',
            new_name='activityEditedOn',
        ),
    ]