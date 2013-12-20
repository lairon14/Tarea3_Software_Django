from django.contrib import admin

from demo.apps.clei.models import Persona, Autor, MiembroCP, Topico, Articulo, Evaluacion

admin.site.register(Persona)
admin.site.register(Autor)
admin.site.register(MiembroCP)
admin.site.register(Topico)
admin.site.register(Articulo)
admin.site.register(Evaluacion)