# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-25 23:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=120)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('to do', 'to do'), ('Doing', 'Doing'), ('Done', 'Done')], default='to do', max_length=15)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_bug', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='upvotes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(max_length=160, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.Bug')),
            ],
        ),
    ]
