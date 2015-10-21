from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from fabbricati.models import Ubicazioni, Fabbricato
#from fabbricati.forms import UbicazioneForm
from .forms import Fabbricato as FabbricatoFrom
from .forms import Ubicazioni as UbicazioneForm
from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):

        fabbricati = Fabbricato.objects.all()


        ctx = RequestContext(request,{'fabbricati':fabbricati})
        return render_to_response('pages/index.html',context_instance=ctx)


def fabbricato(request,id_fab):

    class FabbricatoForm(ModelForm):
        class Meta:
            model = Fabbricato
            exclude = ('Nome',)

    fabbricato = Fabbricato.objects.get(id=id_fab)


    form = FabbricatoFrom()
    ctx = RequestContext(request,{'fabbricato':fabbricato, 'form':form})
    return render_to_response('pages/fabbricato.html',context_instance=ctx)


class UbicazioneForm(ModelForm):
    class Meta:
        model = Ubicazioni
        fields = ['Numero_Fabbricato', 'Complesso_Forestale', 'UGB', 'Comune']


def ubicazione(request, id_fab):
    #
    fabbricato = Fabbricato.objects.get(id=id_fab)
    # ubicazione = Ubicazioni.objects.get(id=fabbricato.Ubicazione.id)
    #
    # ctx = RequestContext(request,{'ubicazione':ubicazione, 'fabbricato':fabbricato})
    # return render_to_response('pages/ubicazione.html',context_instance=ctx)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UbicazioneForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UbicazioneForm()
        ctx = RequestContext(request)
        return render_to_response('pages/ubicazione.html',
                                  locals(),
                                  context_instance=ctx)
