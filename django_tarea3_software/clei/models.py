from django.db import models

from datetime import datetime
    
#clase para registrar un lugar
class Lugar(models.Model):
    nombre = models.CharField( max_length = 100)
    ubicacion = models.CharField( max_length = 250)
    capacidad = models.PositiveIntegerField( default = 0)
        
    def __unicode__(self):
        return "%s %s %i" % (self.nombre, self.ubicacion, self.capacidad)
    
class Evento(models.Model):
    duracion = models.TimeField() #HH:MM:SS
    fecha = models.DateField() # YYYY-MM-DD
    hora_inicio = models.TimeField() # HH:MM:SS
    lugar = models.ForeignKey(Lugar)
    
    def HoraFin(self, inicio, duracion):

        segundos = inicio.second + duracion.second
        minutos = inicio.minute + duracion.minute
        hora = inicio.hour + duracion.hour
        if segundos > 59:
            segundos = segundos - 60
            minutos += 1
        if minutos > 59:
            minutos = minutos - 60
            hora += 1
        if hora > 23:
            hora = hora - 24
      
        return datetime.strptime(str(hora)+":"+str(minutos)+":"+str(segundos), "%H:%M:%S").time()
   

    def __unicode__(self):
        return "%s %s %s %s" % (self.duracion, self.fecha, self.hora_inicio, self.lugar)
    
class Taller(Evento):
    nombre = models.CharField( max_length = 30)
    
    def obtener_segunda_fecha(self, fecha):
        
        DiasPorMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dia = fecha.day + 1
        mes = fecha.month
        ano = fecha.year
        #numero de dias que tiene el mes 'mes'
        aux = DiasPorMes[mes]
        #si dias es mayor que dias por mes actual
        if aux >= dia:
            return datetime.strptime(str(ano)+"-"+str(mes)+"-"+str(dia), '%Y-%m-%d').date()
        else:
            if aux == 30:
                dia -= 30
                mes += 1
            elif aux == 31:
                dia -= 31
                if mes == 12:
                    ano += 1
                    mes = 1
                else:
                    mes += 1
            else:
                dia -= 28
                mes += 1
        return datetime.strptime(str(ano)+"-"+str(mes)+"-"+str(dia), '%Y-%m-%d').date()
    
    def __unicode__(self):
        return "%s" % (self.nombre)
    
class Eventos_Sociales(Evento):
    nombre = models.CharField( max_length = 30)
    
    def __unicode__(self):
        return "%s" % (self.nombre)

class Apertura(Evento):
    nombre = models.CharField( max_length = 30)
    
    def obtener_fecha(self, fecha):
        
        DiasPorMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        dia = fecha.day + 4
        mes = fecha.month
        ano = fecha.year
        
        #numero de dias que tiene el mes 'mes'
        aux = DiasPorMes[mes]
        
        #si dias es mayor que dias por mes actual
        if aux >= dia:
            return datetime.strptime(str(ano)+"-"+str(mes)+"-"+str(dia), '%Y-%m-%d').date()
        else:
            if aux == 30:
                dia -= 30
                mes += 1
            elif aux == 31:
                dia -= 31
                if mes == 12:
                    ano += 1
                    mes = 1
                else:
                    mes += 1
            else:
                dia -= 28
                mes += 1
                    
                
        return datetime.strptime(str(ano)+"-"+str(mes)+"-"+str(dia), '%Y-%m-%d').date()
    
    def __unicode__(self):
        return "%s" % (self.nombre)

class Clausura(Evento):
    nombre = models.CharField( max_length = 30)
    
    
    
    def __unicode__(self):
        return "%s" % (self.nombre) 
    
    
##############################

class Persona(models.Model):
    nombre = models.CharField(max_length = 64)
    apellido = models.CharField(max_length = 64)
    institucion = models.CharField(max_length = 64)
    pais = models.CharField(max_length = 32)
    
    def __unicode__(self):
        return "%s %s %s %s"%(self.nombre, self.apellido, self.institucion, self.pais)

class Topico(models.Model):
    nombre = models.CharField(max_length = 64)
    
    def es_igual(self, nombre_topico):
        return self.nombre == nombre_topico
    
    def __unicode__(self):
        return "%s" %(self.nombre)

class MiembroCP(Persona):
    topico = models.ManyToManyField(Topico, null=True, blank = True)
    es_presidente = models.BooleanField(default = False)
    
    def Obtener_topico(self, topico):
        lista = self.topico.all()
        for top in lista:
            if top == topico:
                return 1
        return 0
    
    def Topicos(self):
        return self.topico.all()
    
    def __unicode__(self):
        nombre_completo = "%s" %(self.nombre)
        return nombre_completo
    
class CharlistaInvitado(Persona):
    curriculum = models.CharField( max_length = 100 )
        
    def __unicode__(self):
        return "%s" % (self.curriculum)
    

class Charlas_Invitadas(Evento):
    nombre = models.CharField( max_length = 30)
    resumen = models.CharField( max_length = 255)
    charlista = models.ForeignKey(CharlistaInvitado)
    cp = models.ForeignKey(MiembroCP)
    topico = models.ForeignKey(Topico)
        
    def __unicode__(self):
        return "%s %s %s %s" % (self.nombre, self.resumen, self.charlista, self.cp)
    
class Articulo(models.Model):
    TIPOS_DE_ESTADOS = (
                        ('ACEPTADO', 'ACEPTADO'),
                        ('ACEPTADO_ESPECIAL', "ACEPTADO_ESPECIAL"),
                        ('RECHAZADO POR FALTA DE CUPO', 'RECHAZADO POR FALTA DE CUPO'),
                        ('RECHAZADO POR FALTA DE PROMEDIO','RECHAZADO POR FALTA DE PROMEDIO'),
                        ('SIN DECIDIR', 'SIN DECIDIR'),                      
                        )
    titulo = models.CharField(max_length = 64)
    p1 = models.CharField(max_length = 20)
    p2 = models.CharField(max_length = 20, null = True)
    p3 = models.CharField(max_length = 20, null = True)
    p4 = models.CharField(max_length = 20, null = True)
    p5 = models.CharField(max_length = 20, null = True)
    topicos = models.ManyToManyField(Topico)
    autores = models.ManyToManyField(Persona)
    status = models.CharField(max_length = 32,
                              choices = TIPOS_DE_ESTADOS,
                              default="SIN DECIDIR")
      
    def Verificar_topico(self, cp_topicos):
        for top in cp_topicos:
            lista = self.topicos.all()
            for t in lista:
                if top == t:
                    return 1
        return 0
                
                
    def __unicode__(self):
        return self.titulo
    
class Sesiones_Ponencia(Evento):
    nombre = models.CharField( max_length = 30)
    resumen = models.CharField( max_length = 255)
    articulo = models.ForeignKey(Articulo)
    cp = models.ForeignKey(MiembroCP)
    
    def obtener_fecha_ponencia(self, fecha,aux):
        
        DiasPorMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dia = fecha.day + aux
        mes = fecha.month
        ano = fecha.year
        #numero de dias que tiene el mes 'mes'
        aux = DiasPorMes[mes]
        #si dias es mayor que dias por mes actual
        if aux >= dia:
            return datetime.strptime(str(ano)+"-"+str(mes)+"-"+str(dia), '%Y-%m-%d').date()
        else:
            if aux == 30:
                dia -= 30
                mes += 1
            elif aux == 31:
                dia -= 31
                if mes == 12:
                    ano += 1
                    mes = 1
                else:
                    mes += 1
            else:
                dia -= 28
                mes += 1
        return datetime.strptime(str(ano)+"-"+str(mes)+"-"+str(dia), '%Y-%m-%d').date()
    
    def __unicode__(self):
        return "%s %s %s %s" % (self.nombre, self.resumen, self.articulo, self.cp)
    
