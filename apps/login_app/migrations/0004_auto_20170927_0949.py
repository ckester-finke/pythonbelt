# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20170927_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
    ]
