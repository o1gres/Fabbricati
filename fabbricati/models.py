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

    # def __unicode__(self):
    #     return self.Numero_Fabbricato

    # class Meta:
    #     verbose_name = "Ubicazioni"
    #     verbose_name_plural = "Ubicazioni"


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


#class CaratteristicheCostruttive SI CREA UNA TABELLA DI CARATTERISTICHE?

#class cCopertura SI CREA UNA TABELLA DI CARATTERISTICHE?

class AltriElementiCostruttivi(models.Model):
    Solai = models.CharField (max_length=20, null=True, blank=True)
    Tamponature = models.CharField (max_length=20, null=True, blank=True)
    FinestreLuciPorte = models.CharField (max_length=20, null=True, blank=True)
    PavimentazionePrevalente  = models.CharField (max_length=20, null=True, blank=True)
    NumeroServiziIgenici = models.IntegerField (null=True, blank=True)
    RenditaPresunta = models.FloatField ()
    RenditaRivalutata5  = models.FloatField ()
    Coefficiente = models.FloatField ()
    Imponibile = models.FloatField ()


    def __unicode__(self):
        return self.Solai

    class Meta:
        verbose_name = "Altri Elementi Costruttivi"
        verbose_name_plural = "Altri Elementi Costruttivi"



class Fabbricato(models.Model):
    Nome = models.CharField(max_length=30, blank=True, null=True ,verbose_name="Nome Fabbricato")
    Ubicazione = models.ForeignKey(Ubicazioni, related_name="Ubicazione", null=True, blank=True,verbose_name="Ubicazione")
    ElementoCatastale = models.ForeignKey(ElementiCatastali, related_name="ElementoCatastale", null=True, blank=True,verbose_name="Elemento Catastale")
    RiferimentoTemporale = models.ForeignKey(RiferimentiTemporali, related_name="RiferimentoTemporale", null=True, blank=True,verbose_name="Riferimento Temporale")
    RiferimentoYuppie =  models.ForeignKey(RiferimentiYuppies, related_name="RiferimentoYuppie", null=True, blank=True,verbose_name="Riferimento Yuppie")
    CaratteristicaTecnicha =  models.ForeignKey(CaratteristicheTecniche, related_name="CaratteristicaTecnica", null=True, blank=True,verbose_name="Caratteristica Tecnica")
    DatiMetrici =  models.ForeignKey(DatiMetrici, related_name="DatoMetrico", null=True, blank=True,verbose_name="Dato Metrico")
    AltriElementiCostruttivi = models.ForeignKey(AltriElementiCostruttivi, related_name="AltriElementiCostruttivi", null=True, blank=True,verbose_name="Altri Elementi Costruttivi")

    # Nome = models.CharField(max_length=30, blank=True, null=True ,verbose_name="Nome Fabbricato")
    # Numero_Fabbricato = models.CharField(max_length=30, unique=True,)
    # Complesso_Forestale = models.CharField(max_length=30, unique=True,)
    # UGB = models.CharField(max_length=30, unique=True,)
    # Comune = models.CharField(max_length=30, unique=True,)
    # Localita = models.CharField(max_length=30, unique=True,)
    # #Aggiungere campo destinazione come hiave estera di una tabella destinazioni
    #
    #
    # Fg = models.IntegerField (null=True, blank=True)
    # Particella = models.IntegerField (null=True, blank=True)
    # Sub = models.IntegerField (null=True, blank=True)
    # Cat = models.CharField (max_length=6, null=True, blank=True)
    # SuperficieCatastale = models.CharField (max_length=20, null=True, blank=True)
    # Rendita = models.FloatField ()
    # Tecnico = models.CharField (max_length=20, null=True, blank=True) #prenderli da una tabella contenete un elenco di tecnici???
    # Data = models.DateTimeField(blank=True, null=True)
    #
    #
    # AnnoDiCostruzione = models.IntegerField()  #Puo non essere riempito?
    # AnnoDiRistrutturazione = models.IntegerField()
    # StatoUso = models.CharField (max_length=20)
    #
    #
    # Docfa = models.CharField(max_length=20)
    #
    #
    # ServiziIgenici = models.CharField (max_length=20, null=True, blank=True)
    # VaniTecnologici = models.CharField (max_length=20, null=True, blank=True)
    # EnergiaElettrica = models.CharField (max_length=20, null=True, blank=True)
    # Riscaldamento = models.CharField (max_length=20, null=True, blank=True)
    # AcquaCalda = models.CharField (max_length=20, null=True, blank=True)
    # ApprovvigionamentoIdrico = models.CharField (max_length=20, null=True, blank=True)
    # Reflui = models.CharField (max_length=20, null=True, blank=True)
    # AntennaTV = models.CharField (max_length=20, null=True, blank=True)
    # Collegamenti = models.CharField (max_length=20, null=True, blank=True)
    #
    #
    # PianiFuoriTerra = models.IntegerField (null=True, blank=True)
    # PianiEntroTerraOSemiinterrati = models.IntegerField (null=True, blank=True)
    # SuperficieCoperta = models.IntegerField (null=True, blank=True)
    # SuperficieTotaleSviluppata = models.IntegerField (null=True, blank=True)
    # VolumeTotaleVPP = models.IntegerField (null=True, blank=True)
    #
    #
    # Solai = models.CharField (max_length=20, null=True, blank=True)
    # Tamponature = models.CharField (max_length=20, null=True, blank=True)
    # FinestreLuciPorte = models.CharField (max_length=20, null=True, blank=True)
    # PavimentazionePrevalente  = models.CharField (max_length=20, null=True, blank=True)
    # NumeroServiziIgenici = models.IntegerField (null=True, blank=True)
    # RenditaPresunta = models.FloatField ()
    # RenditaRivalutata5  = models.FloatField ()
    # Coefficiente = models.FloatField ()
    # Imponibile = models.FloatField ()



    # def __unicode__(self):
    #     return self.Nome
    #
    #
    # class Meta:
    #     verbose_name = "Fabbricato"
    #     verbose_name_plural = "Fabbricati"

