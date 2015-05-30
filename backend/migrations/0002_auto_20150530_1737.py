# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50)),
                ('clabe', models.CharField(max_length=50)),
                ('branch_number', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MonetaryDonation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('bank_account', models.ForeignKey(to='backend.BankAccount')),
                ('civil_association', models.ForeignKey(to='backend.CivilAssociation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteeringPledge',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('bank_account', models.ForeignKey(to='backend.BankAccount')),
                ('civil_association', models.ForeignKey(to='backend.CivilAssociation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='civilassociation',
            name='bank_account',
            field=models.ForeignKey(null=True, blank=True, to='backend.BankAccount'),
        ),
    ]
