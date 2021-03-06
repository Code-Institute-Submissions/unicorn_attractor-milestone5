# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-17 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_auto_20200609_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Done', 'Done')], default='Pending', max_length=15),
        ),
    ]
