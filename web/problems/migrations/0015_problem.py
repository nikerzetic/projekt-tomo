# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0014_auto_20160810_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editable', models.BooleanField()),
            ],
            bases=(utils.models.OrderWithRespectToMixin, models.Model),
        ),
    ]
