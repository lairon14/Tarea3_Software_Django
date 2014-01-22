
from django.conf.urls import patterns, url


urlpatterns = patterns = patterns('clei.apps.histograma.views',
        url(r'^histograma/plotResult.png$', 'plot_result', name='plotResult'),
        url(r'^histograma/mostrar$', 'mostrar_histograma_view', name='vista_mostrar_histograma'),
        url(r'^histograma/seleccion$', 'seleccionar_histograma_view', name='vista_seleccionar_histograma'),
       )

