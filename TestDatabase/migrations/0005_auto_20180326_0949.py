# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-26 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestDatabase', '0004_auto_20180326_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='inviter',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
