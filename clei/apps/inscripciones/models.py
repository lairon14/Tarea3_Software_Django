'''
Created on 14/12/2013

@author: ubuntu
'''
from datetime import datetime
from django.db import models

from clei.apps.clei.models import Persona, Evento


class Participante(Persona):

    correo = models.EmailField()
    direcionPostal = models.CharField(max_length=64)
    url = models.URLField(max_length=64)
    codigo_de_area = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    
    def __unicode__(self):
        cadena = "%s %s" % (self.nombre, self.apellido)
#         cadena += " %s %s" % (self.correo, self.numeroTelefono)
        return cadena
    
class ComoInscribir():
    
    fecha_limite = datetime
    costo = int
    descuento = int

    def __init__(self):
        raise NotImplementedError("Excepcion, Esta clase es una Interfaz")
    
    def __unicode__(self):
        cadena = "%s %s" % (self.costo)
#         cadena += " %s %s" % (self.correo, self.numeroTelefono)
        return cadena

class InscribirGeneral(ComoInscribir):
    
    def __init__(self):
        self.fecha_limite = datetime(2014, 01, 31, 11, 00, 00)
        self.costo = 250
        self.descuento = 80
    
    def configurar_inscripcion(self):
        if datetime.now() < self.fecha_limite:
            self.costo = self.costo - self.descuento    
            
class InscribirAcademico(ComoInscribir):
    
    def __init__(self):
        self.fecha_limite = datetime(2015, 01, 31, 11, 00, 00)
        self.costo = 250
        self.descuento = 150
    
    def configurar_inscripcion(self):
            self.costo = self.costo - self.descuento      
    
class Inscripcion(models.Model):
    persona = models.ForeignKey(Participante)
    fecha_inscripcion = models.DateTimeField(default=datetime.now)
    costo = models.PositiveIntegerField(default=0)
    descuento = models.PositiveIntegerField(default=0)
    pago_realizado = models.PositiveIntegerField(default=0)
    numero_de_deposito = models.PositiveIntegerField()
    eventos = models.ManyToManyField(Evento)
    #comprobante_academico = models.FileField(upload_to = '~/Documentos/CI3715/Tarea3_Software_Django/comprobantes')
    
    
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)

    def __unicode__(self):
        insc = "%s %s" % (self.persona.__unicode__(), self.pago_realizado)
        return insc
