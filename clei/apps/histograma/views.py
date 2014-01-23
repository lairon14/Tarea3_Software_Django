
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from clei.apps.clei.models import Articulo

import numpy as np 
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from clei.apps.histograma.models import histograma

def seleccionar_histograma_view(request):
    return render_to_response('histograma/seleccion_histograma.html',
                               context_instance=RequestContext(request))
    
def plot_result(request):
    hist = histograma()
    (autores, valores) = hist.porAutor()
    
    plt.axes((0.1, 0.3, 0.8, 0.6))
    plt.bar(np.arange(len(valores)), valores)
    plt.ylim(0, 100)
    plt.title("Por autor")
    plt.xticks(np.arange(len(autores)), autores, rotation=90)
    plt.show()
    return render_to_response('histograma/seleccion_histograma.html',
                               context_instance=RequestContext(request))
    

def mostrar_histograma_autor_view(request):
    hist = histograma()
    (autores, valores) = hist.porAutor()
    plt.axes((0.1, 0.3, 0.8, 0.6))
    plt.bar(np.arange(len(valores)), valores)
    plt.ylim(0, max(valores)+20)
    plt.title("Histograma de articulos aceptados por autor")
    plt.xticks(np.arange(len(autores)+1), autores, rotation=90)
    plt.show()
    return render_to_response('histograma/seleccion_histograma.html',
                               context_instance=RequestContext(request))
    
def mostrar_histograma_pais_view(request):
    hist = histograma()
    (pais, valores) = hist.porPais()
    plt.axes((0.1, 0.3, 0.8, 0.6))
    plt.bar(np.arange(len(valores)), valores)
    plt.ylim(0, max(valores)+20)
    plt.title("Histograma de articulos aceptados por pais")
    plt.xticks(np.arange(len(pais)+1), pais, rotation=90)
    plt.show()
    return render_to_response('histograma/seleccion_histograma.html',
                               context_instance=RequestContext(request))
    