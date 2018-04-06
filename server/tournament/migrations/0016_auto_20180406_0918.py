# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-06 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0015_tournamentresult_exclude_from_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='display_notes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournamentregistration',
            name='is_highlighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournamentregistration',
            name='notes',
            field=models.TextField(blank=True, default='', help_text='Tell us about yourself', null=True, verbose_name='Notes. Optional'),
        ),
    ]
