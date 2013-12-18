from django.conf.urls import patterns, url 
  
urlpatterns = patterns = patterns('clei.views', 
        url(r'^$', 'index_view', name='vista_principal'), 
        url(r'^registrar/lugar/$', 'registrar_lugar_view', name="vista_registrar_lugar"),
        url(r'^registrar/taller/$', 'registrar_taller_view', name="vista_registrar_taller"), 
        url(r'^registrar/eventoSocial/$', 'registrar_evento_social_view', name="vista_registrar_evento_social"),
        url(r'^registrar/apertura/$', 'registrar_apertura_view', name="vista_registrar_apertura"), 
        url(r'^registrar/clausura/$', 'registrar_clausura_view', name="vista_registrar_clausura"),
        url(r'^registrar/miembrocp/$', 'registrar_miembroCP_view', name="vista_registrar_miembrocp"),
        url(r'^registrar/charlasInvitadas/$', 'registrar_charlasInvitadas_view', name="vista_registrar_charlasInvitadas"),
        url(r'^registrar/charlistaInvitado/$', 'registrar_charlista_view', name="vista_registrar_charlista"),
        url(r'^registrar/articulo/$', 'registrar_articulo_view', name="vista_registrar_articulo"),
        url(r'^registrar/sesionesPonencia/$', 'registrar_sesionesPonencia_view', name="vista_registrar_sesionesPonencia"),
        ) 