# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicazine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Numero_Fabbricato', models.CharField(unique=True, max_length=30)),
                ('Complesso_Forestale', models.CharField(unique=True, max_length=30)),
                ('UGB', models.CharField(unique=True, max_length=30)),
                ('Comune', models.CharField(unique=True, max_length=30)),
                ('Localita', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
