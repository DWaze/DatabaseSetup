# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-27 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestDatabase', '0011_auto_20180327_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='TestDatabase.Group'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='TestDatabase.Person'),
        ),
    ]