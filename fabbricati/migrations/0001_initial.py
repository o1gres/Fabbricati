# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                'verbose_name': 'Altri Elementi Costruttivi',
                'verbose_name_plural': 'Altri Elementi Costruttivi',
            },
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
                'verbose_name': 'Caratteristiche Tecniche',
                'verbose_name_plural': 'Caratteristiche Tecniche',
            },
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
                'verbose_name': 'Dati Metrici',
                'verbose_name_plural': 'Dati Metrici',
            },
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
                'verbose_name': 'Elementi Catastali',
                'verbose_name_plural': 'Elementi Catastali',
            },
        ),
        migrations.CreateModel(
            name='Fabbricato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=30, null=True, verbose_name=b'Nome Fabbricato', blank=True)),
                ('AltriElementiCostruttivi', models.ForeignKey(related_name='AltriElementiCostruttivi', verbose_name=b'Altri Elementi Costruttivi', blank=True, to='fabbricati.AltriElementiCostruttivi', null=True)),
                ('CaratteristicaTecnicha', models.ForeignKey(related_name='CaratteristicaTecnica', verbose_name=b'Caratteristica Tecnica', blank=True, to='fabbricati.CaratteristicheTecniche', null=True)),
                ('DatiMetrici', models.ForeignKey(related_name='DatoMetrico', verbose_name=b'Dato Metrico', blank=True, to='fabbricati.DatiMetrici', null=True)),
                ('ElementoCatastale', models.ForeignKey(related_name='ElementoCatastale', verbose_name=b'Elemento Catastale', blank=True, to='fabbricati.ElementiCatastali', null=True)),
            ],
            options={
                'verbose_name': 'Fabbricato',
                'verbose_name_plural': 'Fabbricati',
            },
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
                'verbose_name': 'Riferimenti Temporali',
                'verbose_name_plural': 'Riferimenti Temporali',
            },
        ),
        migrations.CreateModel(
            name='RiferimentiYuppies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Docfa', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Riferimenti Yuppies',
                'verbose_name_plural': 'Riferimenti Yuppies',
            },
        ),
        migrations.CreateModel(
            name='Ubicazioni',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Numero_Fabbricato', models.CharField(unique=True, max_length=30)),
                ('Complesso_Forestale', models.CharField(unique=True, max_length=30)),
                ('UGB', models.CharField(unique=True, max_length=30)),
                ('Comune', models.CharField(unique=True, max_length=30)),
                ('Localita', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Ubicazione',
                'verbose_name_plural': 'Ubicazioni',
            },
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='RiferimentoTemporale',
            field=models.ForeignKey(related_name='RiferimentoTemporale', verbose_name=b'Riferimento Temporale', blank=True, to='fabbricati.RiferimentiTemporali', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='RiferimentoYuppie',
            field=models.ForeignKey(related_name='RiferimentoYuppie', verbose_name=b'Riferimento Yuppie', blank=True, to='fabbricati.RiferimentiYuppies', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='Ubicazione',
            field=models.ForeignKey(related_name='Ubicazione', verbose_name=b'Ubicazione', blank=True, to='fabbricati.Ubicazioni', null=True),
        ),
    ]
