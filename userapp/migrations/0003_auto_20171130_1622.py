# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-30 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20171130_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemanager',
            name='pm_functional_group',
            field=models.CharField(choices=[('IT-ProjectTeam', 'IT-ProjectTeam'), ('IT-Support', 'IT-Support'), ('Others', 'Others')], max_length=25),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='salutation',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Mdm', 'Mdm'), ('Dr', 'Dr'), ('Past', 'Past'), ('Evan', 'Evan'), ('Prof', 'Prof'), ('Mast', 'Mast'), ('Team', 'Team'), ('Group', 'Group')], default='Mr', max_length=5),
        ),
    ]
