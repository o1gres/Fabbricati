# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ubicazioni',
            options={'verbose_name': 'Ubicazioni', 'verbose_name_plural': 'Ubicazioni'},
        ),
    ]
