from django.shortcuts import render_to_response
from django.template import RequestContext

from demo.apps.clei.forms import RegistrarMiembroCPForm, RegistrarArticuloForm
from demo.apps.clei.forms import RegistrarEvaluacionForm, RegistrarTopicoForm
from demo.apps.clei.forms import RegistrarAutorForm

from demo.apps.clei.models import Evaluacion, Topico, Autor

def index_view(request):
    return render_to_response('index.html',
                               context_instance = RequestContext(request))
    

def registrar_miembroCP_view(request):

    if request.method == 'POST':
        form = RegistrarMiembroCPForm(request.POST)
        if form.is_valid():
            cp = form.save(commit=False)
            cp.nombre = form.cleaned_data["nombre"]
            cp.apellido = form.cleaned_data["apellido"]
            cp.institucion = form.cleaned_data["institucion"]
            cp.pais = form.cleaned_data["pais"]
            cp.save()
            form.save_m2m() # Se guardan los atributod manytomany
            info = "Se guardo satisfactoriamente"
            form = RegistrarMiembroCPForm()
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarMiembroCPForm(request.POST)
                
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarMiembroCP.html', ctx, 
                                    context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarMiembroCPForm()
        ctx = {"form":form}
        return render_to_response('registrarMiembroCP.html', ctx, 
                                       context_instance = RequestContext(request))



def registrar_topico_view(request):

    if request.method == 'POST':
        form = RegistrarTopicoForm(request.POST)
        if form.is_valid():
            topico = Topico()
            topico.nombre = form.cleaned_data["nombre"]
            topico.save()
            info = "Se guardo satisfactoriamente"
            form = RegistrarTopicoForm()
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarTopicoForm(request.POST)
        
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarTopico.html', ctx, 
                                    context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarTopicoForm()
        ctx = {"form":form}
        return render_to_response('registrarTopico.html', ctx, 
                                       context_instance = RequestContext(request))


def registrar_autor_view(request):

    if request.method == 'POST':
        form = RegistrarAutorForm(request.POST)
        if form.is_valid():
            autor = Autor()
            autor.nombre = form.cleaned_data["nombre"]
            autor.apellido = form.cleaned_data["apellido"]
            autor.institucion = form.cleaned_data["institucion"]
            autor.pais = form.cleaned_data["pais"]
            autor.save()
            info = "Se guardo satisfactoriamente"
                
        else:
            info = "Informacion con datos incorrectos"
                
        form = RegistrarAutorForm()
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarAutor.html', ctx, 
                                    context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarAutorForm()
        ctx = {"form":form}
        return render_to_response('registrarAutor.html', ctx, 
                                       context_instance = RequestContext(request))
            
    
def registrar_articulo_view(request):

    if request.method == 'POST':
        form = RegistrarArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.titulo = form.cleaned_data["titulo"]
            articulo.p1 = form.cleaned_data["p1"]
            articulo.p2 = form.cleaned_data["p2"]
            articulo.p3 = form.cleaned_data["p3"]
            articulo.p4 = form.cleaned_data["p4"]
            articulo.p5 = form.cleaned_data["p5"]
            articulo.save()
            form.save_m2m()
            info = "Se guardo satisfactoriamente"
                
        else:
            info = "Informacion con datos incorrectos"
                
        form = RegistrarArticuloForm(request.POST)
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarArticulo.html', ctx, 
                                    context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarArticuloForm()
        ctx = {"form":form}
        return render_to_response('registrarArticulo.html', ctx, 
                                    context_instance = RequestContext(request))
            
    
def registrar_evaluacion_view(request): 
    if request.method == 'POST': # Si la request es POST
        form = RegistrarEvaluacionForm(request.POST)
        if form.is_valid():
            nueva_eval = Evaluacion()
            nueva_eval.articulo = form.cleaned_data["articulo"]
            nueva_eval.miembro_cp = form.cleaned_data["miembro_cp"]
            nueva_eval.nota = form.cleaned_data["nota"]
            nueva_eval.save()
            info = "Se guardo satisfactoriamente"
            form = RegistrarEvaluacionForm()
                
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarEvaluacionForm(request.POST)
                
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarEvaluacion.html', ctx, 
                                    context_instance = RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarEvaluacionForm()
        ctx = {"form":form}
        return render_to_response('registrarEvaluacion.html', ctx, 
                                    context_instance = RequestContext(request))
