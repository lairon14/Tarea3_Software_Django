
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from clei.apps.histograma.models import histograma

def seleccionar_histograma_view(request):
    return render_to_response('histograma/seleccion_histograma.html',
                               context_instance=RequestContext(request))
    
def mostrar_histograma_view(request):
    return render_to_response('histograma/mostrar_histograma.html',
                               context_instance=RequestContext(request))
    

def resultado_histograma_view(request):
    hist = histograma()
    fig = hist.porAutor()
    canvas = FigureCanvas(fig)
    response= HttpResponse(mimetype='image/png')
    canvas.print_png(response)
    return response
    