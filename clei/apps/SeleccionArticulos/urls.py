
from django.conf.urls import patterns, url


urlpatterns = patterns = patterns('clei.apps.SeleccionArticulos.views',
        url(r'^seleccionarticulo/$', 'index_seleccionar_articulos_view', name='vista_index_seleccion_articulo'),
        url(r'^seleccionarticulo/topico/$', 'seleccionar_articulos_topico_view', name='vista_seleccion_articulo_topico'),
        url(r'^seleccionarticulo/cortes/$', 'seleccionar_articulos_cortes_view', name='vista_seleccion_articulo_cortes'),
        url(r'^seleccionarticulo/porcentaje/$', 'seleccionar_articulos_porcentaje_view', name='vista_seleccion_articulo_porcentaje'),
        url(r'^seleccionarticulo/pais/$', 'seleccionar_articulos_min_p_view', name='vista_seleccion_articulo_min_p'),
        url(r'^seleccionarticulo/aceptados_empatados/$', 'seleccionar_articulos_aceptados_empatados_view', name='vista_seleccion_articulo_aceptados_empatados'),
        url(r'^seleccionarticulo/desempate/escogencia/$', 'seleccionar_articulos_desempate_escogencia_view', name='vista_seleccion_articulo_desempate_escogencia'),        
        )
