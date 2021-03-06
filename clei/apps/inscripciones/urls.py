from django.conf.urls import patterns, url

from clei.apps.inscripciones.views import CreateParticipanteView, \
    VerInscripcionView, CreateGeneralView, VerInscritosView, CreateAcademicoView,\
    CreateTalleresView, CreateCharlasView


urlpatterns = patterns('clei.apps.inscripciones.views',
                       url(r'^$', 'index_view', name='vista_inscripciones'),

                       url(r'^create/$', CreateParticipanteView.as_view(), name='crear_participante'),

                       url(r'^paquete/$', 'select_paquete_view', name='vista_seleccion_paquete'),

                       url(r'^vergeneral/$', 'ver_general_view', name='vista_ver_general'),

                       url(r'^veracademico/$', 'ver_academico_view', name='vista_ver_academico'),

                       url(r'^vertalleres/$', 'ver_talleres_view', name='vista_ver_talleres'),

                       url(r'^vercharlas/$', 'ver_charlas_view', name='vista_ver_charlas'),

                       url(r'^general/$', CreateGeneralView.as_view(), name='vista_paquete_general'),

                       url(r'^academico/$', CreateAcademicoView.as_view(), name='vista_paquete_academico'),

                       url(r'^talleres/$', CreateTalleresView.as_view(), name='vista_paquete_talleres'),

                       url(r'^charlas/$', CreateCharlasView.as_view(), name='vista_paquete_charlas'),

                       url(r'^inscritos/$', VerInscritosView.as_view(), name='vista_inscritos'),

                       url(r'^ver/(?P<pk>[\w]+)/$', VerInscripcionView.as_view(), name='ver_inscripcion'),

                       )
