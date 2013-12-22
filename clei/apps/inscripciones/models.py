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
    url = models.CharField(max_length=64)
    numeroTelefono = models.CharField(max_length=64)
    fecha = models.DateTimeField(default=datetime.now())  
    
    def __unicode__(self):
        cadena = "%s %s        %s" % (self.nombre, self.apellido, self.correo)
#         cadena += " %s %s" % (self.correo, self.numeroTelefono)
        return cadena
    
class ComoInscribir(object):
    
    fecha_limite = datetime
    costo = int
    descuento = int

    def __init__(self):
        raise NotImplementedError("Excepcion, Esta clase es una Interfaz")

    def configurar_inscripcion(self):
        raise NotImplementedError("Excepcion, Esta clase es una Interfaz")

class InscribirGeneral(ComoInscribir):
    
    def __init__(self):
        self.fecha_limite = datetime.now()
        self.costo = 250
        self.descuento = 100
    
    def configurar_inscripcion(self):
        if datetime.now()<self.fecha_limite:
            self.costo = self.costo - self.descuento
            
        
        
    
class Inscripcion(models.Model):
    persona = models.ForeignKey(Participante)
    fecha_inscripcion = models.DateTimeField(default=datetime.now)
    costo = models.IntegerField(default=0)
    descuento = models.IntegerField(default=0)
    pago_realizado = models.IntegerField(default=0)
    eventos = models.ManyToManyField(Evento)
    
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
#         self.persona = persona   
    
    def __unicode__(self):
        insc = "%s %s" % (self.persona.__unicode__(), self.pago_realizado)
        return insc
