__author__ = 'sergio'
from django import forms
from django.forms import ModelForm
from fabbricati.models import Fabbricato, Ubicazioni


# class UbicazioneForm(forms.ModelForm):
#
#     class Meta:
#         model = Ubicazioni
#         exclude = ('Numero_Fabbricato',)



# class FabbricatoForm(forms.ModelForm):
#
#     class Meta:
#         model = Fabbricato
#         exclude = ('Nome',)