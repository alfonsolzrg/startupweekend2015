# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20150530_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilassociation',
            name='bank_account',
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='civil_association',
            field=models.ForeignKey(to='backend.CivilAssociation', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civilassociation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 30, 22, 46, 14, 567650, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='civilassociation',
            name='last_modified_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 30, 22, 46, 50, 49900, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
