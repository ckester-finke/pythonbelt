# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_auto_20170927_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friend_id',
            field=models.ManyToManyField(related_name='_user_friend_id_+', to='login_app.User'),
        ),
    ]
