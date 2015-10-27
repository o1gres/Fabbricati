# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0003_auto_20151026_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltriDati',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Accatastato', models.CharField(max_length=50)),
                ('IntestazioneCatastale', models.CharField(max_length=50)),
                ('Utilizzo', models.CharField(max_length=50)),
                ('Costruttore', models.CharField(max_length=50)),
                ('Finanziamento', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Altri Dati',
                'verbose_name_plural': 'Altri Dati',
            },
        ),
        migrations.CreateModel(
            name='CaratteristicheCostruttive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescCaratCostruttive', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Caratteristiche Costruttive',
                'verbose_name_plural': 'Caratteristiche Costruttive',
            },
        ),
        migrations.CreateModel(
            name='Copertura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescCopertura', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Copertura',
                'verbose_name_plural': 'Coperture',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescNote', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Note',
            },
        ),
        migrations.CreateModel(
            name='Provenienza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescProvenienza', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Provenienza',
                'verbose_name_plural': 'Provenienza',
            },
        ),
        migrations.CreateModel(
            name='TipologiaDiAccesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescTipologiaDiAccessoe', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Tipologia di accesso',
                'verbose_name_plural': 'Tipologia di accesso',
            },
        ),
        migrations.CreateModel(
            name='TitoloDiDetenzione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescTitoloDiDetenzione', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Titolo di detenzione',
                'verbose_name_plural': 'Titolo di tdetenzione',
            },
        ),
        migrations.CreateModel(
            name='TitoloDiPossesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescTitoloDiPossesso', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Titolo di possesso',
                'verbose_name_plural': 'Titolo di possesso',
            },
        ),
    ]
