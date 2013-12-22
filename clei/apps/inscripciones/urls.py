from django.conf.urls import patterns, url

from clei.apps.inscripciones.views import CreateParticipanteView, \
    VerInscripcionView, CreateGeneralView, VerInscritosView


urlpatterns = patterns('clei.apps.inscripciones.views',
                       url(r'^$', 'index_view', name='vista_inscripciones'),
                       
                       url(r'^create/$', CreateParticipanteView.as_view(), name='crear_participante'),

                       url(r'^paquete/$', 'select_paquete_view', name='vista_seleccion_paquete'),

                       url(r'^general/$', CreateGeneralView.as_view(), name='vista_paquete_general'),

                       url(r'^inscritos/$', VerInscritosView.as_view(),name='vista_inscritos'),
                       
                       url(r'^ver/(?P<pk>[\w]+)/$', VerInscripcionView.as_view(), name='ver_inscripcion'),
                       
                       )
