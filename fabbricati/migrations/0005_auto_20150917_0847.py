# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0004_altrielementicostruttivi_caratteristichetecniche_datimetrici_elementicatastali_riferimentitemporali_'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='altrielementicostruttivi',
            options={'verbose_name': 'Altri Elementi Costruttivi', 'verbose_name_plural': 'Altri Elementi Costruttivi'},
        ),
        migrations.AlterModelOptions(
            name='caratteristichetecniche',
            options={'verbose_name': 'Caratteristiche Tecniche', 'verbose_name_plural': 'Caratteristiche Tecniche'},
        ),
        migrations.AlterModelOptions(
            name='datimetrici',
            options={'verbose_name': 'Dati Metrici', 'verbose_name_plural': 'Dati Metrici'},
        ),
        migrations.AlterModelOptions(
            name='elementicatastali',
            options={'verbose_name': 'Elementi Catastali', 'verbose_name_plural': 'Elementi Catastali'},
        ),
        migrations.AlterModelOptions(
            name='riferimentitemporali',
            options={'verbose_name': 'Riferimenti Temporali', 'verbose_name_plural': 'Riferimenti Temporali'},
        ),
        migrations.AlterModelOptions(
            name='riferimentiyuppies',
            options={'verbose_name': 'Riferimenti Yuppies', 'verbose_name_plural': 'Riferimenti Yuppies'},
        ),
    ]
