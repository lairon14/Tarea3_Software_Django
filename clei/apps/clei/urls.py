from django.conf.urls import patterns, url


urlpatterns = patterns = patterns('clei.apps.clei.views',
        url(r'^$', 'index_view', name='vista_principal'),
        url(r'^registrar/miembrocp/$', 'registrar_miembroCP_view', name="vista_registrar_miembrocp"),
        url(r'^registrar/articulo/$', 'registrar_articulo_view', name="vista_registrar_articulo"),
        url(r'^registrar/evaluacion/$', 'registrar_evaluacion_view', name="vista_registrar_evaluacion"),
        url(r'^registrar/topico/$', 'registrar_topico_view', name='vista_registrar_topico'),
        url(r'^registrar/autor/$', 'registrar_autor_view', name='vista_registrar_autor'),
        url(r'^registrar/lugar/$', 'registrar_lugar_view', name="vista_registrar_lugar"),
        url(r'^registrar/taller/$', 'registrar_taller_view', name="vista_registrar_taller"),
        url(r'^registrar/eventoSocial/$', 'registrar_evento_social_view', name="vista_registrar_evento_social"),
        url(r'^registrar/apertura/$', 'registrar_apertura_view', name="vista_registrar_apertura"),
        url(r'^registrar/clausura/$', 'registrar_clausura_view', name="vista_registrar_clausura"),
        url(r'^registrar/charlasInvitadas/$', 'registrar_charlasInvitadas_view', name="vista_registrar_charlasInvitadas"),
        url(r'^registrar/charlistaInvitado/$', 'registrar_charlista_view', name="vista_registrar_charlista"),
        url(r'^registrar/sesionesPonencia/$', 'registrar_sesionesPonencia_view', name="vista_registrar_sesionesPonencia"),
        url(r'^programa/conferencia/$', 'generar_programa_view', name="vista_generar_programa"),
        url(r'^actas/conferencia/$', 'generar_actas_view', name="vista_generar_actas"),
        url(r'^registrar/ListarArticulos/$','Listar_ArticulosporSesion_view',name = "vista_ListarArticulos"),
        )


