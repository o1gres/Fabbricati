# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0005_auto_20151026_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caratteristichecostruttive',
            name='DescCaratCostruttive',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
