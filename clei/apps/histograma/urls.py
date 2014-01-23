
from django.conf.urls import patterns, url


urlpatterns = patterns = patterns('clei.apps.histograma.views',
        url(r'^histograma/plotResult.png$', 'plot_result', name='plotResult'),
        url(r'^histograma/mostrar/autor$', 'mostrar_histograma_autor_view', name='vista_mostrar_histograma_autor'),
        url(r'^histograma/mostrar/pais$', 'mostrar_histograma_pais_view', name='vista_mostrar_histograma_pais'),
        url(r'^histograma/seleccion$', 'seleccionar_histograma_view', name='vista_seleccionar_histograma'),
       )

