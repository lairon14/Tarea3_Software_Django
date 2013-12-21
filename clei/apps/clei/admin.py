from django.contrib import admin

from clei.apps.clei.models import Apertura, Charlas_Invitadas, CharlistaInvitado, \
    Clausura, Eventos_Sociales, Lugar, Persona, Autor, MiembroCP, Topico, Articulo, \
    Evaluacion, Sesiones_Ponencia, Taller


# Registro de modelos
admin.site.register(Persona)
admin.site.register(Autor)
admin.site.register(MiembroCP)
admin.site.register(Topico)
admin.site.register(Articulo)
admin.site.register(Evaluacion)
admin.site.register(Lugar)
admin.site.register(Taller)
admin.site.register(Eventos_Sociales)
admin.site.register(Apertura)
admin.site.register(Clausura)
admin.site.register(Charlas_Invitadas)
admin.site.register(CharlistaInvitado)
admin.site.register(Sesiones_Ponencia)
