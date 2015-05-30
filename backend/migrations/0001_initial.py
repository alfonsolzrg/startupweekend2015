# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CivilAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('founded_in', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('contact_email', models.EmailField(max_length=254, default='', blank=True)),
                ('legal_representative', models.CharField(max_length=200, default='', blank=True)),
                ('logo', models.ImageField(upload_to='', blank=True, null=True)),
                ('facebook_url', models.CharField(max_length=255, default='', blank=True)),
                ('twitter_url', models.CharField(max_length=255, default='', blank=True)),
                ('instagram_url', models.CharField(max_length=255, default='', blank=True)),
                ('category', models.ForeignKey(to='backend.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='civilassociation',
            name='tags',
            field=models.ManyToManyField(to='backend.Tag'),
        ),
    ]
