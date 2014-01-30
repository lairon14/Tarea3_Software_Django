from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from clei.apps.clei.models import Evento, Taller, Charlas_Invitadas, Persona,\
    CharlistaInvitado, MiembroCP, Autor
from clei.apps.inscripciones.forms import ParticipanteForm, \
    InscripcionGeneralForm
from clei.apps.inscripciones.models import Participante, Inscripcion, \
    InscribirGeneral, InscribirAcademico, InscribirTalleres, InscribirCharlas
from clei.apps import inscripciones


def index_view(request):
    return render_to_response('inscripciones/index.html',
                            context_instance=RequestContext(request))


def select_paquete_view(request):
    return render_to_response('inscripciones/select_paquete.html',
                              context_instance=RequestContext(request))


def ver_general_view(request):
    return render_to_response('inscripciones/ver_general.html',
                              context_instance=RequestContext(request))


def ver_academico_view(request):
    return render_to_response('inscripciones/ver_academico.html',
                              context_instance=RequestContext(request))


def ver_talleres_view(request):
    return render_to_response('inscripciones/ver_talleres.html',
                              context_instance=RequestContext(request))


def ver_charlas_view(request):
    return render_to_response('inscripciones/ver_charlas.html',
                              context_instance=RequestContext(request))


class CreateAcademicoView(CreateView):
    persona = None
    model = Inscripcion
    form_class = InscripcionGeneralForm
    template_name = "inscripciones/paquete_academico.html"
    tipoInscripcion = InscribirAcademico()
    # tipoInscripcion.configurar_inscripcion()

    initial = {'pago_realizado': tipoInscripcion.costo - tipoInscripcion.descuento, 'persona' :Participante.objects.last(), 'costo':tipoInscripcion.costo, 'descuento':tipoInscripcion.descuento, 'fecha_inscripcion':datetime.now, 'eventos': Evento.objects.all()}

    def get_context_data(self, *args, **kwargs):
        context = super(CreateAcademicoView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_inscripcion', args=[self.object.id])


class CreateGeneralView(CreateView):
    persona = None
    model = Inscripcion
    form_class = InscripcionGeneralForm
    template_name = "inscripciones/paquete_general.html"
    tipoInscripcion = InscribirGeneral()
    tipoInscripcion.configurar_inscripcion()
    initial = {'pago_realizado': tipoInscripcion.costo - tipoInscripcion.descuento, 'persona' :Participante.objects.last(), 'costo':tipoInscripcion.costo, 'descuento':tipoInscripcion.descuento, 'fecha_inscripcion':datetime.now, 'eventos': Evento.objects.all()}

    def get_context_data(self, *args, **kwargs):
        context = super(CreateGeneralView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_inscripcion', args=[self.object.id])


class CreateTalleresView(CreateView):
    persona = None
    model = Inscripcion
    form_class = InscripcionGeneralForm
    template_name = "inscripciones/paquete_talleres.html"
    tipoInscripcion = InscribirTalleres()
    tipoInscripcion.configurar_inscripcion()
    initial = {'pago_realizado': tipoInscripcion.costo - tipoInscripcion.descuento, 'persona' :Participante.objects.last(), 'costo':tipoInscripcion.costo, 'descuento':tipoInscripcion.descuento, 'fecha_inscripcion':datetime.now, 'eventos': Taller.objects.all()}

    def get_context_data(self, *args, **kwargs):
        context = super(CreateTalleresView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_inscripcion', args=[self.object.id])


class CreateCharlasView(CreateView):
    persona = None
    model = Inscripcion
    form_class = InscripcionGeneralForm
    template_name = "inscripciones/paquete_charlas.html"
    tipoInscripcion = InscribirCharlas()
    tipoInscripcion.configurar_inscripcion()

    initial = {'pago_realizado': tipoInscripcion.costo - tipoInscripcion.descuento, 'persona' :Participante.objects.last(), 'costo':tipoInscripcion.costo, 'descuento':tipoInscripcion.descuento, 'fecha_inscripcion':datetime.now, 'eventos': Charlas_Invitadas.objects.all()}

    def get_context_data(self, *args, **kwargs):
        context = super(CreateCharlasView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_inscripcion', args=[self.object.id])


class CreateParticipanteView(CreateView):
    model = Participante
    form_class = ParticipanteForm 
    template_name = "inscripciones/create_participante.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CreateParticipanteView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('vista_seleccion_paquete')


class VerInscripcionView(DetailView):
    model = Inscripcion
    template_name = "inscripciones/ver_inscripcion.html"


class VerInscritosView(ListView):
    context_object_name = 'vista_inscritos'
    template_name = "inscripciones/ver_inscritos.html"
    queryset = Persona.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VerInscritosView, self).get_context_data(**kwargs)
        context['inscripciones'] = Inscripcion.objects.all()
        context['charlistas'] = CharlistaInvitado.objects.all()
        context['miembrocp'] = MiembroCP.objects.all()
        context['autores'] = Autor.objects.all()
        return context
