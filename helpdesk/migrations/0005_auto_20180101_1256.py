# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-01 04:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_ticket_attach2project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='assigned_manager',
            new_name='assigned_admin',
        ),
    ]