from django.db import models

# Create your models here.
class Ubicazione(models.Model):

    Numero_Fabbricato = models.CharField(max_length=30, unique=True,)
    Complesso_Forestale = models.CharField(max_length=30, unique=True,)
    UGB = models.CharField(max_length=30, unique=True,)
    Comune = models.CharField(max_length=30, unique=True,)
    Localita = models.CharField(max_length=30, unique=True,)
    #Aggiungere campo destinazione come hiave estera di una tabella destinazioni

    def __unicode__(self):
        return self.Numero_Fabbricato

    class Meta:
        verbose_name = "Ubicazione"
        verbose_name_plural = "Ubicazioni"