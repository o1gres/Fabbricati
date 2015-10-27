from django.apps import apps
from django.contrib import admin
from django.db import models
from .models import Fabbricato, Ubicazioni, ElementiCatastali, RiferimentiTemporali, RiferimentiYuppies, \
                    CaratteristicheTecniche, DatiMetrici
from django.contrib.admin.sites import AlreadyRegistered

# admin.site.register(Fabbricato)
# admin.site.register(Ubicazioni)
# admin.site.register(ElementiCatastali)
# admin.site.register(RiferimentiTemporali)
# admin.site.register(RiferimentiYuppies)
# admin.site.register(CaratteristicheTecniche)
# admin.site.register(DatiMetrici)


#register dinamically all modules in admin instead of register eachone manually
app_models = apps.get_app_config('fabbricati').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass