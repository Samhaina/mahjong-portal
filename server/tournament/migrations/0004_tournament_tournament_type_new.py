# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_tournamentregistration_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tournament_type_new',
            field=models.CharField(choices=[['rr', 'rr'], ['crr', 'crr'], ['ema', 'ema'], ['fema', 'fema'], ['other', 'other']], default='rr', max_length=10),
        ),
    ]
