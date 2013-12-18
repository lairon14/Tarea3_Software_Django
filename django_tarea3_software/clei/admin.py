from django.contrib import admin
from clei.models import Lugar
from clei.models import Taller
from clei.models import Eventos_Sociales
from clei.models import Apertura
from clei.models import Clausura
from clei.models import MiembroCP
from clei.models import Topico
from clei.models import Charlas_Invitadas
from clei.models import CharlistaInvitado
from clei.models import Articulo
from clei.models import Sesiones_Ponencia

# Registro mis clases de models
admin.site.register(Lugar)
admin.site.register(Taller)
admin.site.register(Eventos_Sociales)
admin.site.register(Apertura)
admin.site.register(Clausura)
admin.site.register(MiembroCP)
admin.site.register(Topico)
admin.site.register(Charlas_Invitadas)
admin.site.register(CharlistaInvitado)
admin.site.register(Articulo)
admin.site.register(Sesiones_Ponencia)