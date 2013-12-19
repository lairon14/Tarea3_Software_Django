from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from demo.apps.clei.models import Articulo

from demo.apps.SeleccionArticulos.forms import NForm, CortesForm, MinPForm
from demo.apps.SeleccionArticulos.models import ArticuloPorcentaje, ArticuloPaisesDesempate
from demo.apps.SeleccionArticulos.models import ArticuloTopico, ArticuloCortes, ArticuloDesempate

def index_seleccionar_articulos_view(request):
    return render_to_response('seleccionarArticulos.html',
                               context_instance = RequestContext(request))

def seleccionar_articulos_aceptados_empatados_view(request):
    if request.method == 'POST':
        form = NForm(request.POST)
        if form.is_valid():
                
            n = form.cleaned_data["n"]
            info = "Se guardo satisfactoriamente con valor = ", n
            #articulos = Articulo.objects.all()
            estrategia = ArticuloDesempate(n)
            articulos = estrategia.seleccionar_articulos()
            n_restantes = articulos_restantes_por_aceptar(articulos,n)
            ctx = {"articulos":articulos, "informacion":info, "n_por_decidir":n_restantes}
            return render_to_response('listarArticulosDesempate.html', ctx, 
                                       context_instance = RequestContext(request))
                
        else:
            info = "Informacion con datos incorrectos"
            form = NForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('seleccionarArticuloParametros.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = NForm()
        ctx = {"form":form}
        return render_to_response('seleccionarArticuloParametros.html', ctx, 
        context_instance = RequestContext(request))
 
def articulos_restantes_por_aceptar(lista_de_articulos,n):
    n_restantes = 0
    for art in lista_de_articulos:
        if art.status == 'ACEPTADO':
            n_restantes += 1            
    return n - n_restantes

def articulos_restantes_por_decidir(lista_de_articulos):
    n_decidir = 0
    for art in lista_de_articulos:
        if art.status == 'POR DECIDIR':
            n_decidir += 1            
    return n_decidir


def seleccionar_articulos_min_p_view(request):
    if request.method == 'POST':
        form = MinPForm(request.POST)
        if form.is_valid():
                
            n = form.cleaned_data["n"]
            p = form.cleaned_data["min_p"]
            info = "Se guardo satisfactoriamente con valor = ", n
            #articulos = Articulo.objects.all()
            estrategia = ArticuloPaisesDesempate(n, p)
            articulos = estrategia.seleccionar_articulos()
            ctx = {"articulos":articulos, "informacion":info}
            return render_to_response('listarArticulos.html', ctx, 
                                       context_instance = RequestContext(request))
                
        else:
            info = "Informacion con datos incorrectos"
            form = MinPForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('seleccionarArticuloParametros.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = MinPForm()
        ctx = {"form":form}
        return render_to_response('seleccionarArticuloParametros.html', ctx, 
        context_instance = RequestContext(request))    

        
def seleccionar_articulos_cortes_view(request):
    if request.method == 'POST':
        form = CortesForm(request.POST)
        if form.is_valid():
                
            n = form.cleaned_data["n"]
            corte1 = form.cleaned_data["corte1"]
            corte2 = form.cleaned_data["corte2"]
            if corte1 <= corte2 or corte1 <= 3.0 or corte2 < 3.0:
                if corte1 <= 3.0 or corte2 < 3.0:
                    info = "El primer corte debe ser mayor que 3.0 y el segundo mayor o igual a 3.0"
                else:
                    info = "El primer corte debe ser mayor al segundo"
                form = CortesForm()
                ctx = {"form":form, "informacion":info}
                return render_to_response('seleccionarArticuloParametros.html', ctx, 
                                           context_instance = RequestContext(request))
            
                
            info = "Se guardo satisfactoriamente con valor = ", n
            articulos = Articulo.objects.all()
            estrategia = ArticuloCortes(n, corte1, corte2)
            articulos = estrategia.seleccionar_articulos()
            ctx = {"articulos":articulos, "informacion":info}
            return render_to_response('listarArticulos.html', ctx, 
                                       context_instance = RequestContext(request))
                
        else:
            info = "Informacion con datos incorrectos"
            form = CortesForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('seleccionarArticuloParametros.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = CortesForm()
        ctx = {"form":form}
        return render_to_response('seleccionarArticuloParametros.html', ctx, 
        context_instance = RequestContext(request))
        
        
def seleccionar_articulos_porcentaje_view(request):
    if request.method == 'POST':
        form = NForm(request.POST)
        if form.is_valid():
                
            n = form.cleaned_data["n"]
            info = "Se guardo satisfactoriamente con valor = ", n
            #articulos = Articulo.objects.all()
            estrategia = ArticuloPorcentaje(n)
            articulos = estrategia.seleccionar_articulos()
            ctx = {"articulos":articulos, "informacion":info}
            return render_to_response('listarArticulos.html', ctx, 
                                       context_instance = RequestContext(request))
                
        else:
            info = "Informacion con datos incorrectos"
            form = NForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('seleccionarArticuloParametros.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = NForm()
        ctx = {"form":form}
        return render_to_response('seleccionarArticuloParametros.html', ctx, 
        context_instance = RequestContext(request))
    
def seleccionar_articulos_topico_view(request):
    if request.method == 'POST':
        form = NForm(request.POST)
        if form.is_valid():
                
            n = form.cleaned_data["n"]
            info = "Se guardo satisfactoriamente con valor = ", n
            #articulos = Articulo.objects.all()
            estrategia = ArticuloTopico(n)
            articulos = estrategia.seleccionar_articulos()
            ctx = {"articulos":articulos, "informacion":info}
            return render_to_response('listarArticulos.html', ctx, 
                                       context_instance = RequestContext(request))
                
        else:
            info = "Informacion con datos incorrectos"
            form = NForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('seleccionarArticuloParametros.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = NForm()
        ctx = {"form":form}
        return render_to_response('seleccionarArticuloParametros.html', ctx, 
        context_instance = RequestContext(request))
    
def seleccionar_articulos_desempate_escogencia_view(request):
    if request.method == 'POST':
        post = request.POST
        elegidos = post.getlist('empatados')
        for nombre_articulo in elegidos:
            elegido = Articulo.objects.filter(titulo = nombre_articulo)[0]
            elegido.status = 'ACEPTADO ESPECIAL'
            elegido.save()
        articulos = Articulo.objects.all()
        for art in articulos:
            if art.status == 'POR DECIDIR':
                art.status = 'RECHAZADO POR FALTA DE CUPO'
                art.save()
        
        ctx = {"articulos" : articulos }
        return render_to_response('listarArticulosSeleccionPresidente.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        return HttpResponseRedirect('index.html')