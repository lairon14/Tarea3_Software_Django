
from clei.apps.clei.models import Articulo
import numpy as np 
import matplotlib.pyplot as plt

class histograma():
    
    def porAutor(self):
        lista_art_aceptados = Articulo.objects.filter(status='ACEPTADO')
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
        lista_art_aceptados = Articulo.objects.filter(status='ACEPTADO')
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
        pass
        
    def porTopicos(self):
        pass