
from django.contrib import admin

from clei.apps.clei.models import Persona, Autor, MiembroCP, Topico, Articulo, Evaluacion
from clei.apps.clei.models import Lugar
from clei.apps.clei.models import Taller
from clei.apps.clei.models import Eventos_Sociales
from clei.apps.clei.models import Apertura
from clei.apps.clei.models import Clausura
from clei.apps.clei.models import Charlas_Invitadas
from clei.apps.clei.models import CharlistaInvitado
from clei.apps.clei.models import Sesiones_Ponencia

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