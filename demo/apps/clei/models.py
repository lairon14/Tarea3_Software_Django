from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class Persona(models.Model):
    nombre = models.CharField(max_length = 64)
    apellido = models.CharField(max_length = 64)
    institucion = models.CharField(max_length = 64)
    pais = models.CharField(max_length = 32)
    
    def __unicode__(self):
        nombre_completo = "%s %s"%(self.nombre, self.apellido)
        return nombre_completo
    
class Autor(Persona):
    pass

class Topico(models.Model):
    nombre = models.CharField(max_length = 64)
    
    def es_igual(self, topico):
        return self.nombre == topico.nombre
    
    def __unicode__(self):
        return self.nombre

class MiembroCP(Persona):
    topico = models.ManyToManyField(Topico, null=True, blank = True)
    es_presidente = models.BooleanField(default = False)
    
    def __unicode__(self):
        nombre_completo = "%s %s"%(self.nombre, self.apellido)
        return nombre_completo
    
    
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
    autores = models.ManyToManyField(Autor)
    status = models.CharField(max_length = 32,
                              choices = TIPOS_DE_ESTADOS,
                              default="SIN DECIDIR")
    
    def es_aceptable(self):
        evaluaciones = Evaluacion.objects.filter(articulo=self)
        return len(evaluaciones) >= 2 and self.calcular_promedio() >= 3.0
            
    
    def calcular_promedio(self):
        evaluaciones = Evaluacion.objects.filter(articulo=self)
        suma = sum([eva.nota for eva in evaluaciones])
        try:
            promedio = float(suma) / float(len(evaluaciones))
        except ZeroDivisionError:
            promedio = 0
        return promedio
    
    def pertenece_a_pais(self, pais):
        pais.capitalize()
        for autor in self.autores.all():
            if autor.pais == pais:
                return True
        return False
    
        
    def __unicode__(self):
        return self.titulo
     
    
class Evaluacion(models.Model):
    miembro_cp = models.ForeignKey(MiembroCP)
    articulo = models.ForeignKey(Articulo)
    nota = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    #nota = models.IntegerField()
    
    # Funcion que calcula si los topicos del cp
    # y los del articulo coinciden
    def coinciden_topicos(self):
        topicos_articulo = self.articulo.topicos.all()
        topicos_cp = self.miembro_cp.topico.all()
        interseccion = list(set(topicos_articulo) & set(topicos_cp))
        return len(interseccion) > 0
    
    # Funcion que indica si ya existe
    # una evaluacion igual a la actual
    def existe_evaluacion(self):
        repetido = Evaluacion.objects.filter(miembro_cp=self.miembro_cp,
                                             articulo=self.articulo)
        return len(repetido) > 0
        

    