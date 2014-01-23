
from clei.apps.clei.models import Articulo
import numpy as np 
import matplotlib.pyplot as plt
from django.db.models import Q

class histograma():

    
    def porAutor(self):
        lista_art_aceptados = Articulo.objects.filter(Q(status='ACEPTADO') 
                                                           | Q(status="ACEPTADO ESPECIAL"))
        lista_autores = []
        for art in lista_art_aceptados:
            lista_autores += art.autores.all() 
            
        lista_autores = list(set(lista_autores))
        valores=[]
        for a in lista_autores:
            index = 0
            for art in lista_art_aceptados:
                for aut in art.autores.all():
                    if a.nombre == aut.nombre:
                        index+=1
                
            valores.append(index)
        
        return (lista_autores, valores)
        

    def porPais(self):
        lista_art_aceptados = Articulo.objects.filter(Q(status='ACEPTADO') 
                                                           | Q(status="ACEPTADO ESPECIAL"))
        lista_paises = []
        for art in lista_art_aceptados:
            for aut in art.autores.all():
                lista_paises.append(aut.pais) 
            
        lista_paises = list(set(lista_paises))
        valores=[]
        for pais in lista_paises:
            index = 0
            for art in lista_art_aceptados:
                for aut in art.autores.all():
                    if pais == aut.pais:
                        index+=1
                
            valores.append(index)
        
        return (lista_paises, valores)
    
    def porInstitucion(self):
        lista_art_aceptados = Articulo.objects.filter(Q(status='ACEPTADO') 
                                                           | Q(status="ACEPTADO ESPECIAL"))
        lista_institucion = []
        for art in lista_art_aceptados:
            for aut in art.autores.all():
                lista_institucion.append(aut.institucion) 
            
        lista_institucion = list(set(lista_institucion))
        valores=[]
        for inst in lista_institucion:
            index = 0
            for art in lista_art_aceptados:
                for aut in art.autores.all():
                    if inst == aut.institucion:
                        index+=1
                
            valores.append(index)
        
        return (lista_institucion, valores)
        
    def porTopico(self):
        lista_art_aceptados = Articulo.objects.filter(Q(status='ACEPTADO') 
                                                           | Q(status="ACEPTADO ESPECIAL"))
        lista_topicos = []
        for art in lista_art_aceptados:
            lista_topicos += art.topicos.all() 
            
        lista_topicos = list(set(lista_topicos))
        valores=[]
        for t in lista_topicos:
            index = 0
            for art in lista_art_aceptados:
                for top in art.topicos.all():
                    if t.nombre == top.nombre:
                        index+=1
                
            valores.append(index)
        
        return (lista_topicos, valores)
        
        
        