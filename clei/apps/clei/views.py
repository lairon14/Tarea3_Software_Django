from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.http import HttpResponse
from django.db.models import Q


import cStringIO as StringIO
from clei.apps.clei.forms import RegistrarApertura, RegistrarClausura, \
    RegistrarAutorForm, RegistrarLugar, RegistrarCharlistaInvitado, \
    RegistrarSesionesPonencia, RegistrarEvaluacionForm, RegistrarTopicoForm, \
    RegistrarMiembroCPForm, RegistrarArticuloForm, RegistrarTaller, \
    Registrar_Eventos_Sociales, RegistrarCharlasInvitadas
from clei.apps.clei.models import Evento, Taller, Apertura, Clausura, MiembroCP, \
    Articulo, Evaluacion, Topico, Autor, Sesiones_Ponencia, Charlas_Invitadas
import ho.pisa as pisa


def index_view(request):
    return render_to_response('index.html',
                               context_instance=RequestContext(request))
    

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
            form.save_m2m()  # Se guardan los atributod manytomany
            info = "Se guardo satisfactoriamente"
            form = RegistrarMiembroCPForm()
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarMiembroCPForm(request.POST)
                
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarMiembroCP.html', ctx,
                                    context_instance=RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarMiembroCPForm()
        ctx = {"form":form}
        return render_to_response('registrarMiembroCP.html', ctx,
                                       context_instance=RequestContext(request))



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
                                    context_instance=RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarTopicoForm()
        ctx = {"form":form}
        return render_to_response('registrarTopico.html', ctx,
                                       context_instance=RequestContext(request))


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
                                    context_instance=RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarAutorForm()
        ctx = {"form":form}
        return render_to_response('registrarAutor.html', ctx,
                                       context_instance=RequestContext(request))
            
    
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
            form = RegistrarArticuloForm()
                
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarArticuloForm(request.POST)
                
        ctx = {"form":form, "informacion":info}
        return render_to_response('registrarArticulo.html', ctx,
                                    context_instance=RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarArticuloForm()
        ctx = {"form":form}
        return render_to_response('registrarArticulo.html', ctx,
                                    context_instance=RequestContext(request))
            
    
def registrar_evaluacion_view(request): 
    if request.method == 'POST':  # Si la request es POST
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
                                    context_instance=RequestContext(request))
        # Si el request es un GET    
    else:
        form = RegistrarEvaluacionForm()
        ctx = {"form":form}
        return render_to_response('registrarEvaluacion.html', ctx,
                                    context_instance=RequestContext(request))
        
        
def registrar_lugar_view(request):

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
            form = RegistrarLugar()
             
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarLugar(request.POST)
             
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarLugar.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarLugar()
        ctx = {"form":form}
        return render_to_response('RegistrarLugar.html', ctx,
                                   context_instance=RequestContext(request))
             

def registrar_taller_view(request):
    num_aperturas = Apertura.objects.count()
    
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
                # para cada evento verifico que taller a registrar tenga
                # horas, lugar y fecha disponible para registrarse
                for evento in lista_evento:
                    # si ya existe un evento en la misma fecha
                    if evento.fecha == taller.fecha:
                        # si ya existe un evento en el mismo lugar
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
                    form = RegistrarTaller()
            else:
                info = "Los talleres se realizan los primeros dos dias de la Conferencia. Le sugerimos %s o %s" % (fecha_apertura, fecha)  
                form = RegistrarTaller(request.POST)
        else:
            info = "Informacion con datos incorrectos o introduzca primero el evento apertura "
            form = RegistrarTaller(request.POST)
             
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarTaller.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarTaller()
        ctx = {"form":form}
        return render_to_response('RegistrarTaller.html', ctx,
                                   context_instance=RequestContext(request))  


def registrar_evento_social_view(request):
    num_aperturas = Apertura.objects.count()
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
                # para cada evento verifico que taller a registrar tenga
                # horas, lugar y fecha disponible para registrarse
                for evento in lista_evento:
                    # si ya existe un evento en la misma fecha
                    if evento.fecha == eventos_Sociales.fecha:
                        # si ya existe un evento en el mismo lugar
                        hora_fin_evento = Evento().HoraFin(evento.hora_inicio, evento.duracion)
                        if evento.hora_inicio < eventos_Sociales.hora_inicio and eventos_Sociales.hora_inicio < hora_fin_evento:
                            flag = 1
                if flag:
                    info = "Ya existe un evento social en este horario y fecha."
                else:
                    eventos_Sociales.save()
                    form.save_m2m()
                    info = "Se guardo satisfactoriamente"
                    form = Registrar_Eventos_Sociales()
                    
            else:
                info = "La fecha del evento debe estar entre los cinco dias de la Conferencia"
                form = Registrar_Eventos_Sociales(request.POST)
                 
        else:
            info = "Informacion con datos incorrectos o introduzca primero el evento apertura"
            form = Registrar_Eventos_Sociales(request.POST)
             
        
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarEventosSociales.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = Registrar_Eventos_Sociales()
        ctx = {"form":form}
        return render_to_response('RegistrarEventosSociales.html', ctx,
                                   context_instance=RequestContext(request))
    

def registrar_apertura_view(request):
    
    num_aperturas = Apertura.objects.count()
    
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
            form = RegistrarApertura()
            # print num_aperturas
        else:
            info = "Informacion con datos incorrectos o ya existe un evento apertura"
            form = RegistrarApertura(request.POST)
             
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarApertura.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarApertura()
        ctx = {"form":form}
        return render_to_response('RegistrarApertura.html', ctx,
                                   context_instance=RequestContext(request))
             
    
def registrar_clausura_view(request):
    num_clausuras = Clausura.objects.count()
    num_aperturas = Apertura.objects.count()
    
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
                    form = RegistrarClausura()
                else:
                    info = "Fecha de clausura incorrecta, debe introducir: %s" % fecha
                    form = RegistrarClausura(request.POST)
            else:
                info = "Debe registrar primero el evento de apertura" 
                form = RegistrarClausura(request.POST)
        else:
            info = "Informacion con datos incorrectos  o ya existe un evento de Clausura"
            form = RegistrarClausura(request.POST)
             
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarClausura.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarClausura()
        ctx = {"form":form}
        return render_to_response('RegistrarClausura.html', ctx,
                                   context_instance=RequestContext(request))
            
    
def registrar_charlista_view(request):
    
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
            form = RegistrarCharlistaInvitado()
            
        else:
            info = "Informacion con datos incorrectos"
            form = RegistrarCharlistaInvitado(request.POST)
            
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarCharlistaInvitado.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarCharlistaInvitado()
        ctx = {"form":form}
        return render_to_response('RegistrarCharlistaInvitado.html', ctx,
                                   context_instance=RequestContext(request))
            

def registrar_charlasInvitadas_view(request):
    num_aperturas = Apertura.objects.count()
    
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
                
                lista_evento = Evento.objects.all()
                flag = 0
                
                es_experto = MiembroCP.objects.filter(nombre=charlasInvitadas.cp)[0].Obtener_topico(charlasInvitadas.topico)
                
                if not es_experto:
                    info = "El topico de la charla debe ser igual a la experticia del CP"
                else:
                    # para cada evento verifico que taller a registrar tenga
                    # horas, lugar y fecha disponible para registrarse
                    for evento in lista_evento:
                        # si ya existe un evento en la misma fecha
                        if evento.fecha == charlasInvitadas.fecha:
                            # si ya existe un evento en el mismo lugar
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
                        form = RegistrarCharlasInvitadas()
                
            else:
                info = "La fecha del evento debe estar dentro de los cinco dias de la Conferencia"
                form = RegistrarCharlasInvitadas(request.POST)     
        else:
            info = "Informacion con datos incorrectos o introduzca primero el evento apertura"
            form = RegistrarCharlasInvitadas(request.POST)
             
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarCharlasInvitadas.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarCharlasInvitadas()
        ctx = {"form":form}
        return render_to_response('RegistrarCharlasInvitadas.html', ctx,
                                   context_instance=RequestContext(request))
    
def registrar_sesionesPonencia_view(request):
    num_aperturas = Apertura.objects.count()
    
    if request.method == 'POST':
        form = RegistrarSesionesPonencia(request.POST)
        if form.is_valid() and num_aperturas != 0 :
            
            fecha_apertura = Apertura.objects.values_list()[0][2]
            fecha1 = Sesiones_Ponencia().obtener_fecha_ponencia(fecha_apertura, 2)
                
            fecha2 = Sesiones_Ponencia().obtener_fecha_ponencia(fecha_apertura, 3)
            
            fecha3 = Sesiones_Ponencia().obtener_fecha_ponencia(fecha_apertura, 4)
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
                es_experto = Articulo.objects.filter(id=id_articulo)[0].Verificar_topico(cpp)
                
                lista_evento = Evento.objects.all()
                flag = 0
                
                
                if not es_experto:
                    info = "Algun topico del articulo debe ser igual a la experticia del CP"
                else:
                    
                    # para cada evento verifico que taller a registrar tenga
                    # horas, lugar y fecha disponible para registrarse
                    for evento in lista_evento:
                        # si ya existe un evento en la misma fecha
                        if evento.fecha == sesionesPonencia.fecha:
                            # si ya existe un evento en el mismo lugar
                            if evento.lugar == sesionesPonencia.lugar:
                                hora_fin_evento = Evento().HoraFin(evento.hora_inicio, evento.duracion)
                                if evento.hora_inicio < sesionesPonencia.hora_inicio and sesionesPonencia.hora_inicio < hora_fin_evento:
                                    flag = 1
                    if flag:
                        info = "Ya existe una ponencia en este horario, lugar y fecha" 
                        form = RegistrarSesionesPonencia(request.POST)
                    else:                    
                        sesionesPonencia.save()
                        form.save_m2m()
                        info = "Se guardo satisfactoriamente "
                        form = RegistrarSesionesPonencia()
            else:
                info = "Las sesiones se realizan los siguientes tres dias de la Conferencia. Le sugerimos %s, %s o %s " % (fecha1, fecha2, fecha3)
                form = RegistrarSesionesPonencia(request.POST)     
        else:
            info = "Informacion con datos incorrectos o introduzca primero el evento apertura"
            form = RegistrarSesionesPonencia(request.POST)     
             
        ctx = {"form":form, "informacion":info}
        return render_to_response('RegistrarSesionesPonencia.html', ctx,
                                   context_instance=RequestContext(request))
    # Si el request es un GET    
    else:
        form = RegistrarSesionesPonencia()
        ctx = {"form":form}
        return render_to_response('RegistrarSesionesPonencia.html', ctx,
                                   context_instance=RequestContext(request))
        
def generar_programa_view(request):
    template = loader.get_template('clei/programa_conferencia.html')
    lista_eventos = Evento.objects.all().order_by('fecha', 'hora_inicio')
    
    context = Context({'lista_eventos':lista_eventos,})
    html  = template.render(context)

    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error. No se pudo generar el pdf')

def generar_actas_view(request):
    template = loader.get_template('clei/actas_conferencia.html')
    lista_articulos = Articulo.objects.filter(Q(status='ACEPTADO') 
                                | Q(status="ACEPTADO ESPECIAL"))
    lista_charlas = Charlas_Invitadas.objects.all()
    
    
    context = Context({'lista_articulos':lista_articulos,'lista_charlas':lista_charlas,})
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error. No se pudo generar el pdf')
    
