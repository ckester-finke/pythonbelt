# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(auto_now=True),
        ),
    ]
