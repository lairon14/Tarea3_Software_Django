from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
 
from clei.forms import RegistrarLugar
from clei.forms import RegistrarTaller
from clei.forms import RegistrarApertura
from clei.forms import RegistrarClausura
from clei.forms import Registrar_Eventos_Sociales
from clei.forms import RegistrarMiembroCP
from clei.forms import RegistrarCharlasInvitadas
from clei.forms import RegistrarCharlistaInvitado
from clei.forms import RegistrarArticuloForm
from clei.forms import RegistrarSesionesPonencia
from clei.models import Lugar, Topico
from clei.models import Evento
from clei.models import Taller
from clei.models import Eventos_Sociales
from clei.models import Apertura
from clei.models import Clausura
from clei.models import MiembroCP
from clei.models import CharlistaInvitado
from clei.models import Charlas_Invitadas
from clei.models import Articulo
from clei.models import Sesiones_Ponencia

from django.db.models import Count
from datetime import *

 
# Create your views here.

def index_view(request):
    return render_to_response('Index.html',
                               context_instance = RequestContext(request))
     
 
def registrar_lugar_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarLugar(request.POST)
            if form.is_valid():
                lugar = form.save(commit=False)
                lugar.nombre = form.cleaned_data["nombre"]
                lugar.ubicacion = form.cleaned_data["ubicacion"]
                lugar.capacidad = form.cleaned_data["capacidad"]
                lugar.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                 
            else:
                info = "Informacion con datos incorrectos"
                 
            form = RegistrarLugar()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarLugar.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarLugar()
            ctx = {"form":form}
            return render_to_response('RegistrarLugar.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")
    

def registrar_taller_view(request):
    num_aperturas = Apertura.objects.count()
    
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarTaller(request.POST)
            if form.is_valid() and num_aperturas != 0:
                
                fecha_apertura = Apertura.objects.values_list()[0][2]
                    
                fecha = Taller().obtener_segunda_fecha(fecha_apertura)
                    
                taller = form.save(commit=False)
                    
                if (fecha == form.cleaned_data["fecha"] or fecha_apertura == form.cleaned_data["fecha"]):
                    taller = form.save(commit=False)
                    taller.duracion = form.cleaned_data["duracion"]
                    taller.fecha = form.cleaned_data["fecha"]
                    taller.hora_inicio = form.cleaned_data["hora_inicio"]
                    taller.lugar = form.cleaned_data["lugar"]
                    taller.nombre = form.cleaned_data["nombre"]
                    
                    lista_evento = Evento.objects.all()
                    flag = 0
                    #para cada evento verifico que taller a registrar tenga
                    #horas, lugar y fecha disponible para registrarse
                    for evento in lista_evento:
                        #si ya existe un evento en la misma fecha
                        if evento.fecha  == taller.fecha:
                            #si ya existe un evento en el mismo lugar
                            if evento.lugar == taller.lugar:
                                hora_fin_evento = Evento().HoraFin(evento.hora_inicio, evento.duracion)
                                if evento.hora_inicio < taller.hora_inicio and taller.hora_inicio < hora_fin_evento:
                                    flag = 1
                    if flag:
                        info = "Ya existe un taller en este horario, lugar y fecha."
                    else:
                        taller.save()
                        form.save_m2m()
                        info = "Se guardo satisfactoriamente %s" % evento
                else:
                    info = "Los talleres se realizan los primeros dos dias de la Conferencia. Le sugerimos %s o %s" % (fecha_apertura,fecha)  
                 
            else:
                info = "Informacion con datos incorrectos o introduzca primero el evento apertura "
                 
            form = RegistrarTaller()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarTaller.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarTaller()
            ctx = {"form":form}
            return render_to_response('RegistrarTaller.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")     


def registrar_evento_social_view(request):
    num_aperturas = Apertura.objects.count()
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = Registrar_Eventos_Sociales(request.POST)
            if form.is_valid() and num_aperturas != 0 :
                fecha_apertura = Apertura.objects.values_list()[0][2]                    
                fecha = Apertura().obtener_fecha(fecha_apertura)  
                
                eventos_Sociales = form.save(commit=False)
                
                if (fecha_apertura <= form.cleaned_data["fecha"] and form.cleaned_data["fecha"] <= fecha):
                    eventos_Sociales.duracion = form.cleaned_data["duracion"]
                    eventos_Sociales.fecha = form.cleaned_data["fecha"]
                    eventos_Sociales.hora_inicio = form.cleaned_data["hora_inicio"]
                    eventos_Sociales.lugar = form.cleaned_data["lugar"]
                    eventos_Sociales.nombre = form.cleaned_data["nombre"]
                    
                    lista_evento = Evento.objects.all()
                    flag = 0
                    #para cada evento verifico que taller a registrar tenga
                    #horas, lugar y fecha disponible para registrarse
                    for evento in lista_evento:
                        #si ya existe un evento en la misma fecha
                        if evento.fecha  == eventos_Sociales.fecha:
                            #si ya existe un evento en el mismo lugar
                            hora_fin_evento = Evento().HoraFin(evento.hora_inicio, evento.duracion)
                            if evento.hora_inicio < eventos_Sociales.hora_inicio and eventos_Sociales.hora_inicio < hora_fin_evento:
                                flag = 1
                    if flag:
                        info = "Ya existe un evento social en este horario y fecha."
                    else:
                        eventos_Sociales.save()
                        form.save_m2m()
                        info = "Se guardo satisfactoriamente"
                        
                else:
                    info = "La fecha del evento debe estar entre los cinco dias de la Conferencia"
                     
            else:
                info = "Informacion con datos incorrectos o introduzca primero el evento apertura"
                 
            form = Registrar_Eventos_Sociales()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarEventosSociales.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = Registrar_Eventos_Sociales()
            ctx = {"form":form}
            return render_to_response('RegistrarEventosSociales.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")
    

def registrar_apertura_view(request):
    
    num_aperturas = Apertura.objects.count()
    
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarApertura(request.POST)
            if form.is_valid()  and num_aperturas < 1:
                apertura = form.save(commit=False)
                num_aperturas = Apertura.objects.count()
                apertura.duracion = form.cleaned_data["duracion"]
                apertura.fecha = form.cleaned_data["fecha"]
                apertura.hora_inicio = form.cleaned_data["hora_inicio"]
                apertura.lugar = form.cleaned_data["lugar"]
                apertura.nombre = form.cleaned_data["nombre"]
                
                apertura.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente " 
                #print num_aperturas
            else:
                info = "Informacion con datos incorrectos o ya existe un evento apertura"
                 
            form = RegistrarApertura()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarApertura.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarApertura()
            ctx = {"form":form}
            return render_to_response('RegistrarApertura.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")   
    
def registrar_clausura_view(request):
    num_clausuras = Clausura.objects.count()
    num_aperturas = Apertura.objects.count()
    
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarClausura(request.POST)
            if form.is_valid() and num_clausuras < 1:                
                if num_aperturas != 0:                    
                    fecha_apertura = Apertura.objects.values_list()[0][2]                    
                    fecha = Apertura().obtener_fecha(fecha_apertura)                   
                    clausura = form.save(commit=False)
                    
                    if (fecha == form.cleaned_data["fecha"]):
                    
                        clausura.duracion = form.cleaned_data["duracion"]
                        clausura.fecha = form.cleaned_data["fecha"]
                        clausura.hora_inicio = form.cleaned_data["hora_inicio"]
                        clausura.lugar = form.cleaned_data["lugar"]
                        clausura.nombre = form.cleaned_data["nombre"]
                        
                        clausura.save()
                        form.save_m2m()
                        
                        info = "Se guardo satisfactoriamente"
                    else:
                        info = "Fecha de clausura incorrecta, debe introducir: %s" % fecha
                else:
                    info = "Debe registrar primero el evento de apertura" 
            else:
                info = "Informacion con datos incorrectos  o ya existe un evento de Clausura"
                 
            form = RegistrarClausura()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarClausura.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarClausura()
            ctx = {"form":form}
            return render_to_response('RegistrarClausura.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")   
    
def registrar_miembroCP_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarMiembroCP(request.POST)
            if form.is_valid():
                cp = form.save(commit=False)
                cp.nombre = form.cleaned_data["nombre"]
                cp.apellido = form.cleaned_data["apellido"]
                cp.institucion = form.cleaned_data["institucion"]
                cp.pais = form.cleaned_data["pais"]
                cp.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarMiembroCP()
            ctx = {"form":form, "informacion":info}
            return render_to_response('registrarMiembroCP.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarMiembroCP()
            ctx = {"form":form}
            return render_to_response('registrarMiembroCP.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")
    
def registrar_charlista_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarCharlistaInvitado(request.POST)
            if form.is_valid():
                charlista = form.save(commit=False)
                charlista.nombre = form.cleaned_data["nombre"]
                charlista.apellido = form.cleaned_data["apellido"]
                charlista.institucion = form.cleaned_data["institucion"]
                charlista.pais = form.cleaned_data["pais"]
                charlista.curriculum = form.cleaned_data["curriculum"]
                charlista.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarCharlistaInvitado()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarCharlistaInvitado.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarCharlistaInvitado()
            ctx = {"form":form}
            return render_to_response('RegistrarCharlistaInvitado.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")

def registrar_charlasInvitadas_view(request):
    num_aperturas = Apertura.objects.count()
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarCharlasInvitadas(request.POST)
            if form.is_valid() and num_aperturas != 0 :
                fecha_apertura = Apertura.objects.values_list()[0][2]                    
                fecha = Apertura().obtener_fecha(fecha_apertura) 
                
                charlasInvitadas = form.save(commit=False)
                
                if (fecha_apertura <= form.cleaned_data["fecha"] and form.cleaned_data["fecha"] <= fecha):
                    charlasInvitadas.duracion = form.cleaned_data["duracion"]
                    charlasInvitadas.fecha = form.cleaned_data["fecha"]
                    charlasInvitadas.hora_inicio = form.cleaned_data["hora_inicio"]
                    charlasInvitadas.lugar = form.cleaned_data["lugar"]
                    charlasInvitadas.nombre = form.cleaned_data["nombre"]
                    charlasInvitadas.resumen = form.cleaned_data["resumen"]
                    charlasInvitadas.charlista = form.cleaned_data["charlista"]
                    charlasInvitadas.cp = form.cleaned_data["cp"]
                    charlasInvitadas.topico = form.cleaned_data["topico"]
                    
                    example = MiembroCP.objects.values_list()
                    
                    lista_evento = Evento.objects.all()
                    flag = 0
                    
                    es_experto = MiembroCP.objects.filter(nombre=charlasInvitadas.cp)[0].Obtener_topico(charlasInvitadas.topico)
                    
                    if not es_experto:
                        info = "El topico de la charla debe ser igual a la experticia del CP"
                    else:
                        #para cada evento verifico que taller a registrar tenga
                        #horas, lugar y fecha disponible para registrarse
                        for evento in lista_evento:
                            #si ya existe un evento en la misma fecha
                            if evento.fecha  == charlasInvitadas.fecha:
                                #si ya existe un evento en el mismo lugar
                                if evento.lugar == charlasInvitadas.lugar:
                                    hora_fin_evento = Evento().HoraFin(evento.hora_inicio, evento.duracion)
                                    if evento.hora_inicio < charlasInvitadas.hora_inicio and charlasInvitadas.hora_inicio < hora_fin_evento:
                                        flag = 1
                        if flag:
                            info = "Ya existe una charla en este horario, lugar y fecha"
                        else:
                            charlasInvitadas.save()
                            form.save_m2m()
                            info = "Se guardo satisfactoriamente"
                    
                else:
                    info = "La fecha del evento debe estar dentro de los cinco dias de la Conferencia"     
            else:
                info = "Informacion con datos incorrectos o introduzca primero el evento apertura"
                 
            form = RegistrarCharlasInvitadas()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarCharlasInvitadas.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarCharlasInvitadas()
            ctx = {"form":form}
            return render_to_response('RegistrarCharlasInvitadas.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")       
    
def registrar_articulo_view(request):
    if request.user.is_authenticated():
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
                #articulo.status = form.cleaned_data["status"]
                articulo.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarArticuloForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('registrarArticulo.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarArticuloForm()
            ctx = {"form":form}
            return render_to_response('registrarArticulo.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")   
    
def registrar_sesionesPonencia_view(request):
    num_aperturas = Apertura.objects.count()
    
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarSesionesPonencia(request.POST)
            if form.is_valid() and num_aperturas !=0 :
                
                fecha_apertura = Apertura.objects.values_list()[0][2]
                fecha1 = Sesiones_Ponencia().obtener_fecha_ponencia(fecha_apertura,2)
                    
                fecha2 = Sesiones_Ponencia().obtener_fecha_ponencia(fecha_apertura,3)
                
                fecha3 = Sesiones_Ponencia().obtener_fecha_ponencia(fecha_apertura,4)
                sesionesPonencia = form.save(commit=False)
                    
                if (fecha1 == form.cleaned_data["fecha"] or fecha2 == form.cleaned_data["fecha"] or fecha3 == form.cleaned_data["fecha"]):
                
                    sesionesPonencia.duracion = form.cleaned_data["duracion"]
                    sesionesPonencia.fecha = form.cleaned_data["fecha"]
                    sesionesPonencia.hora_inicio = form.cleaned_data["hora_inicio"]
                    sesionesPonencia.lugar = form.cleaned_data["lugar"]
                    sesionesPonencia.nombre = form.cleaned_data["nombre"]
                    sesionesPonencia.resumen = form.cleaned_data["resumen"]
                    sesionesPonencia.articulo = form.cleaned_data["articulo"]
                    sesionesPonencia.cp = form.cleaned_data["cp"]
                    
                    
                    id_articulo = Articulo.objects.filter(titulo=sesionesPonencia.articulo)[0].id
                    cpp = MiembroCP.objects.filter(nombre=sesionesPonencia.cp)[0].Topicos()
                    es_experto =  Articulo.objects.filter(id= id_articulo)[0].Verificar_topico(cpp)
                    
                    lista_evento = Evento.objects.all()
                    flag = 0
                    
                    
                    if not es_experto:
                        info = "Algun topico del articulo debe ser igual a la experticia del CP"
                    else:
                        
                        #para cada evento verifico que taller a registrar tenga
                        #horas, lugar y fecha disponible para registrarse
                        for evento in lista_evento:
                            #si ya existe un evento en la misma fecha
                            if evento.fecha  == sesionesPonencia.fecha:
                                #si ya existe un evento en el mismo lugar
                                if evento.lugar == sesionesPonencia.lugar:
                                    hora_fin_evento = Evento().HoraFin(evento.hora_inicio, evento.duracion)
                                    if evento.hora_inicio < sesionesPonencia.hora_inicio and sesionesPonencia.hora_inicio < hora_fin_evento:
                                        flag = 1
                        if flag:
                            info = "Ya existe una ponencia en este horario, lugar y fecha" 
                        else:                    
                            sesionesPonencia.save()
                            form.save_m2m()
                            info = "Se guardo satisfactoriamente"
                else:
                    info = "Las sesiones se realizan los siguientes tres dias de la Conferencia. Le sugerimos %s, %s o %s " %(fecha1,fecha2,fecha3)     
            else:
                info = "Informacion con datos incorrectos o introduzca primero el evento apertura"
                 
            form = RegistrarSesionesPonencia()
            ctx = {"form":form, "informacion":info}
            return render_to_response('RegistrarSesionesPonencia.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarSesionesPonencia()
            ctx = {"form":form}
            return render_to_response('RegistrarSesionesPonencia.html', ctx, 
                                       context_instance = RequestContext(request))
             
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")   