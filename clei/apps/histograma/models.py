
from clei.apps.clei.models import Articulo
import numpy as np 
import matplotlib.pyplot as plt

class histograma():
    
    def porAutor(self):
        lista_art_aceptados = Articulo.objects.filter(status='ACEPTADO')
        autores = ['Juan', 'Erick']
        plt.axes((0.1, 0.3, 0.8, 0.6))
        plt.bar(np.arange(2), lista_art_aceptados)
        plt.ylim(0, 100)
        plt.title("Por autor")
        plt.xticks(np.arange(2), autores, rotation=90)
        return plt.figure()
        
        

    def porPais(self):
        pass
    
    def porInstitucion(self):
        pass
        
    def porTopicos(self):
        pass