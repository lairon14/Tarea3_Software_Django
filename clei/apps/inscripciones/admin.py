from django.contrib import admin

from clei.apps.inscripciones.models import Participante, Inscripcion


admin.site.register(Inscripcion)
admin.site.register(Participante)
# admin.site.register(TipoDeInscripcion)
# admin.site.register(TipoDeDescuento)
# Register your models here.
