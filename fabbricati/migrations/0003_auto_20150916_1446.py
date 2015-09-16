# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0002_auto_20150916_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ubicazione',
            options={'verbose_name': 'Ubicazione', 'verbose_name_plural': 'Ubicazioni'},
        ),
    ]
