# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-18 11:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0005_auto_20200617_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='contributions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='features.Feature'),
        ),
        migrations.RemoveField(
            model_name='feature',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='feature',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='feature_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]