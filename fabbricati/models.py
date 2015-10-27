from django.db import models
from django.contrib import admin


# Create your models here.
from django.utils.translation.trans_real import blankout


class Ubicazioni(models.Model):

    Numero_Fabbricato = models.CharField(max_length=30, unique=True,)
    Complesso_Forestale = models.CharField(max_length=30, unique=True,)
    UGB = models.CharField(max_length=30, unique=True,)
    Comune = models.CharField(max_length=30, unique=True,)
    Localita = models.CharField(max_length=30, unique=True,)
    #Aggiungere campo destinazione come hiave estera di una tabella destinazioni

    def __unicode__(self):
        return self.UGB

    class Meta:
        verbose_name = "Ubicazioni"
        verbose_name_plural = "Ubicazioni"


class ElementiCatastali(models.Model):

    Fg = models.IntegerField (null=True, blank=True)
    Particella = models.IntegerField (null=True, blank=True)
    Sub = models.IntegerField (null=True, blank=True)
    Cat = models.CharField (max_length=6, null=True, blank=True)
    SuperficieCatastale = models.CharField (max_length=20, null=True, blank=True)
    Rendita = models.FloatField ()
    Tecnico = models.CharField (max_length=20, null=True, blank=True) #prenderli da una tabella contenete un elenco di tecnici???
    Data = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.Fg)

    class Meta:
        verbose_name = "Elementi Catastali"
        verbose_name_plural = "Elementi Catastali"




class RiferimentiTemporali(models.Model):
    AnnoDiCostruzione = models.IntegerField()  #Puo non essere riempito?
    AnnoDiRistrutturazione = models.IntegerField()
    StatoUso = models.CharField (max_length=20)

    def __unicode__(self):
        return self.StatoUso

    class Meta:
        verbose_name = "Riferimenti Temporali"
        verbose_name_plural = "Riferimenti Temporali"


class RiferimentiYuppies(models.Model):
    Docfa = models.CharField(max_length=20)

    def __unicode__(self):
        return self.Docfa

    class Meta:
        verbose_name = "Riferimenti Yuppies"
        verbose_name_plural = "Riferimenti Yuppies"


class CaratteristicheTecniche(models.Model):
    ServiziIgenici = models.CharField (max_length=20, null=True, blank=True)
    VaniTecnologici = models.CharField (max_length=20, null=True, blank=True)
    EnergiaElettrica = models.CharField (max_length=20, null=True, blank=True)
    Riscaldamento = models.CharField (max_length=20, null=True, blank=True)
    AcquaCalda = models.CharField (max_length=20, null=True, blank=True)
    ApprovvigionamentoIdrico = models.CharField (max_length=20, null=True, blank=True)
    Reflui = models.CharField (max_length=20, null=True, blank=True)
    AntennaTV = models.CharField (max_length=20, null=True, blank=True)
    Collegamenti = models.CharField (max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.VaniTecnologici

    class Meta:
        verbose_name = "Caratteristiche Tecniche"
        verbose_name_plural = "Caratteristiche Tecniche"



class DatiMetrici(models.Model):
    PianiFuoriTerra = models.IntegerField (null=True, blank=True)
    PianiEntroTerraOSemiinterrati = models.IntegerField (null=True, blank=True)
    SuperficieCoperta = models.IntegerField (null=True, blank=True)
    SuperficieTotaleSviluppata = models.IntegerField (null=True, blank=True)
    VolumeTotaleVPP = models.IntegerField (null=True, blank=True)


    def __unicode__(self):
        return unicode(self.PianiFuoriTerra)

    class Meta:
        verbose_name = "Dati Metrici"
        verbose_name_plural = "Dati Metrici"



class AltriElementiCostruttivi(models.Model):
    Solai = models.CharField (max_length=20, null=True, blank=True)
    Tamponature = models.CharField (max_length=20, null=True, blank=True)
    FinestreLuciPorte = models.CharField (max_length=20, null=True, blank=True)
    PavimentazionePrevalente  = models.CharField (max_length=20, null=True, blank=True)
    NumeroServiziIgenici = models.IntegerField (null=True, blank=True)
    RenditaPresunta = models.FloatField()
    RenditaRivalutata5  = models.FloatField()
    Coefficiente = models.FloatField()
    Imponibile = models.FloatField()


    def __unicode__(self):
        return self.Solai

    class Meta:
        verbose_name = "Altri Elementi Costruttivi"
        verbose_name_plural = "Altri Elementi Costruttivi"



#RIPRENDERE DA QUI CON LA PARTE WEB 26/10/2016


class CaratteristicheCostruttive(models.Model):
    DescCaratCostruttive = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.DescCaratCostruttive

    class Meta:
        verbose_name = "Caratteristiche Costruttive"
        verbose_name_plural = "Caratteristiche Costruttive"



class Copertura(models.Model):
    DescCopertura = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.DescCopertura

    class Meta:
        verbose_name = "Copertura"
        verbose_name_plural = "Coperture"




class AltriDati(models.Model):
    Accatastato = models.CharField(max_length=50)
    IntestazioneCatastale = models.CharField(max_length=50)
    Utilizzo = models.CharField(max_length=50)
    Costruttore = models.CharField(max_length=50)
    Finanziamento = models.CharField(max_length=50)

    def __unicode__(self):
        return self.Utilizzo

    class Meta:
        verbose_name = "Altri Dati"
        verbose_name_plural = "Altri Dati"



class TitoloDiPossesso(models.Model):
    DescTitoloDiPossesso = models.CharField(max_length=60)

    def __unicode__(self):
        return self.DescTitoloDiPossesso

    class Meta:
        verbose_name = "Titolo di possesso"
        verbose_name_plural = "Titolo di possesso"





class Provenienza(models.Model):
    DescProvenienza = models.CharField(max_length=60)

    def __unicode__(self):
        return self.DescProvenienza

    class Meta:
        verbose_name = "Provenienza"
        verbose_name_plural = "Provenienza"




class TitoloDiDetenzione(models.Model):
    DescTitoloDiDetenzione = models.CharField(max_length=60)

    def __unicode__(self):
        return self.DescTitoloDiDetenzione

    class Meta:
        verbose_name = "Titolo di detenzione"
        verbose_name_plural = "Titolo di tdetenzione"




class TipologiaDiAccesso(models.Model):
    DescTipologiaDiAccessoe = models.CharField(max_length=60)

    def __unicode__(self):
        return self.DescTipologiaDiAccessoe

    class Meta:
        verbose_name = "Tipologia di accesso"
        verbose_name_plural = "Tipologia di accesso"




class Note(models.Model):
    DescNote = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.DescNote

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Note"




class Fabbricato(models.Model):
    Nome = models.CharField(max_length=30, blank=True, null=True ,verbose_name="Nome Fabbricato")
    Ubicazione = models.ForeignKey(Ubicazioni, related_name="Ubicazione", null=True, blank=True,verbose_name="Ubicazione")
    ElementoCatastale = models.ForeignKey(ElementiCatastali, related_name="ElementoCatastale", null=True, blank=True,verbose_name="Elemento Catastale")
    RiferimentoTemporale = models.ForeignKey(RiferimentiTemporali, related_name="RiferimentoTemporale", null=True, blank=True,verbose_name="Riferimento Temporale")
    RiferimentoYuppie =  models.ForeignKey(RiferimentiYuppies, related_name="RiferimentoYuppie", null=True, blank=True,verbose_name="Riferimento Yuppie")
    CaratteristicaTecnicha =  models.ForeignKey(CaratteristicheTecniche, related_name="CaratteristicaTecnica", null=True, blank=True,verbose_name="Caratteristica Tecnica")
    DatiMetrici =  models.ForeignKey(DatiMetrici, related_name="DatoMetrico", null=True, blank=True,verbose_name="Dato Metrico")
    AltriElementiCostruttivi = models.ForeignKey(AltriElementiCostruttivi, related_name="AltriElementiCostruttivi", null=True, blank=True,verbose_name="Altri Elementi Costruttivi")
    CaratteristicheCostruttive = models.ForeignKey(CaratteristicheCostruttive, related_name="CaratteristicheCostruttive", null=True, blank=True,verbose_name="Caratteristiche Costruttive")
    Copertura = models.ForeignKey(Copertura, related_name="Copertura", null=True, blank=True,verbose_name="Copertura")
    AltriDati = models.ForeignKey(AltriDati, related_name="AltriDati", null=True, blank=True,verbose_name="AltriDati")
    TitoloDiPossesso = models.ForeignKey(TitoloDiPossesso, related_name="TitoloDiPossesso", null=True, blank=True,verbose_name="Titolo Di Possesso")
    Provenienza = models.ForeignKey(Provenienza, related_name="Provenienza", null=True, blank=True,verbose_name="Provenienza")
    TitoloDiDetenzione = models.ForeignKey(TitoloDiDetenzione, related_name="TitoloDiDetenzione", null=True, blank=True,verbose_name="Titolo Di Detenzione")
    TipologiaDiAccesso = models.ForeignKey(TipologiaDiAccesso, related_name="TipologiaDiAccesso", null=True, blank=True,verbose_name="Tipologia Di Accesso")
    Note = models.ForeignKey(Note, related_name="Note", null=True, blank=True,verbose_name="Note")