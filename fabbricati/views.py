from django.contrib.auth.decorators import login_required


from django.shortcuts import render, render_to_response
from fabbricati.decorator import active_and_login_required
from django.template.context import RequestContext
from fabbricati.models import Ubicazioni, Fabbricato, ElementiCatastali, RiferimentiTemporali, RiferimentiYuppies, \
    CaratteristicheTecniche, DatiMetrici, AltriElementiCostruttivi
#from fabbricati.forms import UbicazioneForm
from .forms import Fabbricato as FabbricatoFrom
from .forms import Ubicazioni as UbicazioneForm
from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def index(request):

        fabbricati = Fabbricato.objects.all()


        ctx = RequestContext(request,{'fabbricati':fabbricati})
        return render_to_response('pages/index.html',context_instance=ctx)


@login_required
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
        fields = ['Numero_Fabbricato', 'Complesso_Forestale', 'UGB', 'Comune', 'Localita']


@login_required
def ubicazione(request, id_fab):
    #
    fabbricato = Fabbricato.objects.get(id=id_fab)
    ubicazione = Ubicazioni.objects.get(id=fabbricato.Ubicazione.id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = UbicazioneForm(request.POST or None, instance=ubicazione)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'ubicazione_id': fabbricato.id})
            return render_to_response('pages/ubicazione.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UbicazioneForm(instance=ubicazione)
        ctx = RequestContext(request, {'ubicazione_id': fabbricato.id})
        return render_to_response('pages/ubicazione.html',
                                  locals(),
                                  context_instance=ctx)


class ElementiCatastaliForm(ModelForm):
    class Meta:
        model = ElementiCatastali
        fields = '__all__'


@login_required
def elementi_catastali(request, id_fab):
    #
    fabbricato = Fabbricato.objects.get(id=id_fab)
    elemento_catastale = ElementiCatastali.objects.get(id=fabbricato.Ubicazione.id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = ElementiCatastaliForm(request.POST or None, instance=elemento_catastale)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'ele_cat_id': fabbricato.id})
            return render_to_response('pages/elementocatastale.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ElementiCatastaliForm(instance=elemento_catastale)
        ctx = RequestContext(request, {'ele_cat_id': fabbricato.id})
        return render_to_response('pages/elementocatastale.html',
                                  locals(),
                                  context_instance=ctx)




class RiferimentiTemporaliForm(ModelForm):
    class Meta:
        model = RiferimentiTemporali
        fields = '__all__'


@login_required
def riferimenti_temporali(request, id_fab):
    #
    fabbricato = Fabbricato.objects.get(id=id_fab)
    riferimento_temporale = RiferimentiTemporali.objects.get(id=fabbricato.RiferimentoTemporale.id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = RiferimentiTemporaliForm(request.POST or None, instance=riferimento_temporale)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'rif_temp_id': fabbricato.id})
            return render_to_response('pages/riferimentitemporali.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RiferimentiTemporaliForm(instance=riferimento_temporale)
        ctx = RequestContext(request, {'rif_temp_id': fabbricato.id})
        return render_to_response('pages/riferimentitemporali.html',
                                  locals(),
                                  context_instance=ctx)




class RiferimentiYuppiesForm(ModelForm):
    class Meta:
        model = RiferimentiYuppies
        fields = '__all__'


@login_required
def riferimentiyuppies(request, id_fab):
    #
    fabbricato = Fabbricato.objects.get(id=id_fab)
    riferimento_yuppies = RiferimentiYuppies.objects.get(id=fabbricato.RiferimentoYuppie.id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = RiferimentiYuppiesForm(request.POST or None, instance=riferimento_yuppies)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'rif_yup_id': fabbricato.id})
            return render_to_response('pages/riferimentiyuppies.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RiferimentiYuppiesForm(instance=riferimento_yuppies)
        ctx = RequestContext(request, {'rif_yup_id': fabbricato.id})
        return render_to_response('pages/riferimentiyuppies.html',
                                  locals(),
                                  context_instance=ctx)




class CaratteristicheTecnicheForm(ModelForm):
    class Meta:
        model = CaratteristicheTecniche
        fields = '__all__'


@login_required
def caratteristichetecniche(request, id_fab):

    fabbricato = Fabbricato.objects.get(id=id_fab)
    caratteristiche_tecniche = CaratteristicheTecniche.objects.get(id=fabbricato.CaratteristicaTecnicha.id)


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = CaratteristicheTecnicheForm(request.POST or None, instance=caratteristiche_tecniche)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'car_tec_id': fabbricato.id})
            return render_to_response('pages/caratteristichetecniche.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CaratteristicheTecnicheForm(instance=caratteristiche_tecniche)
        ctx = RequestContext(request, {'car_tec_id': fabbricato.id})
        return render_to_response('pages/caratteristichetecniche.html',
                                  locals(),
                                  context_instance=ctx)




class DatiMetriciForm(ModelForm):
    class Meta:
        model = DatiMetrici
        fields = '__all__'


@login_required
def datimetrici(request, id_fab):

    fabbricato = Fabbricato.objects.get(id=id_fab)
    dati_metrici = DatiMetrici.objects.get(id=fabbricato.DatiMetrici.id)


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = DatiMetriciForm(request.POST or None, instance=dati_metrici)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'dati_met_id': fabbricato.id})
            return render_to_response('pages/datimetrici.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DatiMetriciForm(instance=dati_metrici)
        ctx = RequestContext(request, {'dati_met_id': fabbricato.id})
        return render_to_response('pages/datimetrici.html',
                                  locals(),
                                  context_instance=ctx)




class AltriElementiCostruttiviForm(ModelForm):
    class Meta:
        model = AltriElementiCostruttivi
        fields = '__all__'


@login_required
def altrielementicostruttivi(request, id_fab):


    fabbricato = Fabbricato.objects.get(id=id_fab)
    altri_elementi_costruttivi = AltriElementiCostruttivi.objects.get(id=fabbricato.AltriElementiCostruttivi.id)


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = AltriElementiCostruttiviForm(request.POST or None, instance=altri_elementi_costruttivi)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ctx = RequestContext(request, {'altri_elem_id': fabbricato.id})
            return render_to_response('pages/altrielementicostruttivi.html',
                                  locals(),
                                  context_instance=ctx)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AltriElementiCostruttiviForm(instance=altri_elementi_costruttivi)
        ctx = RequestContext(request, {'altri_elem_id': fabbricato.id})
        return render_to_response('pages/altrielementicostruttivi.html',
                                  locals(),
                                  context_instance=ctx)