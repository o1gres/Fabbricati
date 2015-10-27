# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabbricati', '0004_altridati_caratteristichecostruttive_copertura_note_provenienza_tipologiadiaccesso_titolodidetenzion'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabbricato',
            name='AltriDati',
            field=models.ForeignKey(related_name='AltriDati', verbose_name=b'AltriDati', blank=True, to='fabbricati.AltriDati', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='CaratteristicheCostruttive',
            field=models.ForeignKey(related_name='CaratteristicheCostruttive', verbose_name=b'Caratteristiche Costruttive', blank=True, to='fabbricati.CaratteristicheCostruttive', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='Copertura',
            field=models.ForeignKey(related_name='Copertura', verbose_name=b'Copertura', blank=True, to='fabbricati.Copertura', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='Note',
            field=models.ForeignKey(related_name='Note', verbose_name=b'Note', blank=True, to='fabbricati.Note', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='Provenienza',
            field=models.ForeignKey(related_name='Provenienza', verbose_name=b'Provenienza', blank=True, to='fabbricati.Provenienza', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='TipologiaDiAccesso',
            field=models.ForeignKey(related_name='TipologiaDiAccesso', verbose_name=b'Tipologia Di Accesso', blank=True, to='fabbricati.TipologiaDiAccesso', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='TitoloDiDetenzione',
            field=models.ForeignKey(related_name='TitoloDiDetenzione', verbose_name=b'Titolo Di Detenzione', blank=True, to='fabbricati.TitoloDiDetenzione', null=True),
        ),
        migrations.AddField(
            model_name='fabbricato',
            name='TitoloDiPossesso',
            field=models.ForeignKey(related_name='TitoloDiPossesso', verbose_name=b'Titolo Di Possesso', blank=True, to='fabbricati.TitoloDiPossesso', null=True),
        ),
    ]
