# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0003_auto_20150916_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltriElementiCostruttivi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Solai', models.CharField(max_length=20, null=True, blank=True)),
                ('Tamponature', models.CharField(max_length=20, null=True, blank=True)),
                ('FinestreLuciPorte', models.CharField(max_length=20, null=True, blank=True)),
                ('PavimentazionePrevalente', models.CharField(max_length=20, null=True, blank=True)),
                ('NumeroServiziIgenici', models.IntegerField(null=True, blank=True)),
                ('RenditaPresunta', models.FloatField()),
                ('RenditaRivalutata5', models.FloatField()),
                ('Coefficiente', models.FloatField()),
                ('Imponibile', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaratteristicheTecniche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ServiziIgenici', models.CharField(max_length=20, null=True, blank=True)),
                ('VaniTecnologici', models.CharField(max_length=20, null=True, blank=True)),
                ('EnergiaElettrica', models.CharField(max_length=20, null=True, blank=True)),
                ('Riscaldamento', models.CharField(max_length=20, null=True, blank=True)),
                ('AcquaCalda', models.CharField(max_length=20, null=True, blank=True)),
                ('ApprovvigionamentoIdrico', models.CharField(max_length=20, null=True, blank=True)),
                ('Reflui', models.CharField(max_length=20, null=True, blank=True)),
                ('AntennaTV', models.CharField(max_length=20, null=True, blank=True)),
                ('Collegamenti', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatiMetrici',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PianiFuoriTerra', models.IntegerField(null=True, blank=True)),
                ('PianiEntroTerraOSemiinterrati', models.IntegerField(null=True, blank=True)),
                ('SuperficieCoperta', models.IntegerField(null=True, blank=True)),
                ('SuperficieTotaleSviluppata', models.IntegerField(null=True, blank=True)),
                ('VolumeTotaleVPP', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElementiCatastali',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fg', models.IntegerField(null=True, blank=True)),
                ('Particella', models.IntegerField(null=True, blank=True)),
                ('Sub', models.IntegerField(null=True, blank=True)),
                ('Cat', models.CharField(max_length=6, null=True, blank=True)),
                ('SuperficieCatastale', models.CharField(max_length=20, null=True, blank=True)),
                ('Rendita', models.FloatField()),
                ('Tecnico', models.CharField(max_length=20, null=True, blank=True)),
                ('Data', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RiferimentiTemporali',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AnnoDiCostruzione', models.IntegerField()),
                ('AnnoDiRistrutturazione', models.IntegerField()),
                ('StatoUso', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RiferimentiYuppies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Docfa', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
