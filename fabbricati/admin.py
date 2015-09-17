from django.contrib import admin
from .models import Ubicazione,ElementiCatastali,RiferimentiTemporali,RiferimentiYuppies,CaratteristicheTecniche,\
                    DatiMetrici


# Register your models here.
admin.site.register(Ubicazione)
admin.site.register(ElementiCatastali)
admin.site.register(RiferimentiTemporali)
admin.site.register(RiferimentiYuppies)
admin.site.register(CaratteristicheTecniche)
admin.site.register(DatiMetrici)