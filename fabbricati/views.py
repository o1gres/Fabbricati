from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from fabbricati.models import *
from .forms import Fabbricato as FabbricatoFrom
from django import forms


# Create your views here.
def index(request):

        fabbricati = Fabbricato.objects.all()



        ctx = RequestContext(request,{'fabbricati':fabbricati})
        return render_to_response('pages/index.html',context_instance=ctx)





