from django.contrib import admin
from django.db import models
from .models import Fabbricato, Ubicazioni, ElementiCatastali, RiferimentiTemporali, RiferimentiYuppies, \
                    CaratteristicheTecniche, DatiMetrici




# Register your models here.


# class FabbricatoAdmin(admin.ModelAdmin):
#     list_display = ('Nome', 'Complesso_Forestale','UGB', 'Comune', 'Localita',)
#     list_filter = ('Nome', 'Complesso_Forestale', 'Comune', 'Localita')
#     search_fields = ('Nome', 'Complesso_Forestale')
#     ordering = ('Nome',)

admin.site.register(Fabbricato)
admin.site.register(Ubicazioni)
admin.site.register(ElementiCatastali)
admin.site.register(RiferimentiTemporali)
admin.site.register(RiferimentiYuppies)
admin.site.register(CaratteristicheTecniche)
admin.site.register(DatiMetrici)