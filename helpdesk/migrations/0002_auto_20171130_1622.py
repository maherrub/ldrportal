# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-30 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpdeskmanager',
            name='hdmgr_functional_group',
            field=models.CharField(choices=[('Servicedesk', 'Servicedesk'), ('IT-Projects', 'IT-Projects'), ('IT-Support', 'IT-Support'), ('Others', 'Others')], max_length=25),
        ),
    ]
