# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_tournament_ema_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='number_of_days',
        ),
        migrations.AlterField(
            model_name='tournament',
            name='clubs',
            field=models.ManyToManyField(blank=True, to='club.Club'),
        ),
    ]