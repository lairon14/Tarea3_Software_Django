
from clei.apps.clei.models import Articulo, Topico,  Autor

class ComoSeleccionarArticulos(object):
    
    __lista_articulos = []
    __num_articulos_aceptar = None
    __lista_rechazados_articulos = []
    
    def __init__(self, num_art_aceptar):
        if not isinstance(num_art_aceptar, int):
            raise TypeError
        if num_art_aceptar <= 0:
            raise ValueError
        self.__lista_rechazados_articulos = []
        articulos_aceptables = []
        for art in Articulo.objects.all():
            if art.es_aceptable():
                articulos_aceptables.append(art)
            else:
                art.status = "RECHAZADO POR FALTA DE PROMEDIO"
             
                self.__lista_rechazados_articulos.append(art)
             
                  
        articulos_aceptables = sorted(articulos_aceptables,
                                       key=lambda x:x.calcular_promedio(),
                                       reverse=True)
        self.__lista_articulos = articulos_aceptables
        self.__num_articulos_aceptar = num_art_aceptar

    def get_lista_articulos(self):
        return self.__lista_articulos
    
    def get_lista_rechazados_articulos(self):
        return self.__lista_rechazados_articulos
    
    def set_lista_articulos(self, value):
        self.__lista_articulos = value
    
    
    def get_num_articulos_aceptar(self):
        return self.__num_articulos_aceptar

    def seleccionar_articulos(self):
        raise NotImplementedError("Excepcion, ComoSeleccionarArticulos se supone que es una interfaz")

# la lista_articulo que se le pasa es una lista de articulos aceptable (prom >= 3)
# por lo que se suponen que todos los articulos que estan aqui son articulos que forman
    
class ArticuloDesempate(ComoSeleccionarArticulos):
        
    def __init__(self, num_art_aceptar):
        super(ArticuloDesempate, self).__init__(num_art_aceptar)
    
    def seleccionar_articulos(self):
        lista_aceptados = []
        lista_empatados = []
        articulos_rechazados_cupo = []
        if len(self.get_lista_articulos()) <= self.get_num_articulos_aceptar():
            lista_aceptados = self.get_lista_articulos()        
        else:
            primeros_n = self.get_lista_articulos()[0 : self.get_num_articulos_aceptar()]
            min_promedio = min([ar.calcular_promedio() for ar in primeros_n])
            empatados = [ar for ar in self.get_lista_articulos() if ar.calcular_promedio() == min_promedio]
            articulos_rechazados_cupo = [ar for ar in self.get_lista_articulos() if ar.calcular_promedio() < min_promedio]
            if len(set(primeros_n) | set(empatados)) == self.get_num_articulos_aceptar():
                lista_aceptados = primeros_n
                lista_empatados = []
            else: 
                if len(empatados) > 1:
                    lista_empatados = empatados
                    lista_aceptados = [ar for ar in primeros_n if ar.calcular_promedio() > min_promedio]
                    for art in lista_empatados:
                        art.status = 'POR DECIDIR'      
                else:
                    lista_aceptados = primeros_n
                    lista_empatados = []
              
        for art in articulos_rechazados_cupo:
            art.status = 'RECHAZADO POR FALTA DE CUPO'  
        for art in lista_aceptados:
            art.status = 'ACEPTADO'
        
        lista_de_salida = lista_aceptados + lista_empatados + articulos_rechazados_cupo + self.get_lista_rechazados_articulos()
        
        for art in Articulo.objects.all():
            for art_salida in lista_de_salida:
                if art.titulo == art_salida.titulo:
                    art.status = art_salida.status
                    art.save()
        
        
        return lista_de_salida
    
                

def calcular_num_participaciones_pais(pais):
    num_participaciones = 0
    for art in Articulo.objects.all():
        lista_paises_del_articulo = [autor.pais for autor in art.autores.all()]
        if pais in lista_paises_del_articulo:
            num_participaciones += 1
    return num_participaciones

class ArticuloPaisesDesempate(ComoSeleccionarArticulos):
    __p = None
    __lista_paises = []
    
    def __init__(self, num_art_aceptar, p):
        super(ArticuloPaisesDesempate, self).__init__(num_art_aceptar)
        if not isinstance(p, int):
            raise TypeError
        if p < 0:
            raise ValueError
        lista_paises = list(set([autor.pais for autor in Autor.objects.all()]))
        # Y la ordenamos en funcion del numero de participaciones
        lista_paises = sorted(lista_paises,
                                       key=lambda x:calcular_num_participaciones_pais(x))
        
        self.__p = p
        self.__lista_paises = lista_paises
        
    def seleccionar_articulos(self):
        lista_seleccionados = []
        # Seleccionamos los p mejores articulos de cada pais 
        for pais in self.__lista_paises:
            lista_articulo_del_pais = [art for art in self.get_lista_articulos() if art.pertenece_a_pais(pais)]  
            lista_articulo_del_pais = sorted(lista_articulo_del_pais,
                                              key = lambda x: x.calcular_promedio()
                                               )
            for i in range(0, self.__p):
                try:
                    articulo_agregar = lista_articulo_del_pais.pop()

                    articulo_agregar.status = 'ACEPTADO'
                    lista_seleccionados.append(articulo_agregar)
                    self.get_lista_articulos().remove(articulo_agregar)
                except:
                    break
                
        # Eliminamos articulos repetidos
        list(set(lista_seleccionados))
        lista_restantes_empatados = []
        
        if len(lista_seleccionados) >= self.get_num_articulos_aceptar():
            lista_rechazados_cupo = lista_seleccionados[self.get_num_articulos_aceptar():]
            lista_seleccionados = lista_seleccionados[0 : self.get_num_articulos_aceptar()]
            for art in lista_rechazados_cupo:
                art.status = 'RECHAZADO POR FALTA DE CUPO'
            
            
            
            return lista_seleccionados + lista_rechazados_cupo + self.get_lista_rechazados_articulos()
        # Si quedan aun articulos por elegir, los elegimos por mejor promedio    
        else:
            num_articulos_por_elegir = self.get_num_articulos_aceptar() - len(lista_seleccionados) 
            
            
            # Si el numero de articulos que quedan es menor al numero de articulos por elegir
            # entonces acetamos a todos los articulos que quedan
            if len(self.get_lista_articulos()) <= num_articulos_por_elegir:
                for art in self.get_lista_articulos():
                    art.status = 'ACEPTADO ESPECIAL'
                lista_seleccionados += self.get_lista_articulos()
                
            else:
                self.set_lista_articulos(sorted(self.get_lista_articulos(),
                                                key=lambda x: x.calcular_promedio(),
                                                reverse=True))
        
                primeros_n = self.get_lista_articulos()[0 : num_articulos_por_elegir]
               
                min_promedio = min([ar.calcular_promedio() for ar in primeros_n])
                lista_restantes_aceptados = [ar for ar in primeros_n if ar.calcular_promedio() > min_promedio]
                lista_restantes_empatados = [ar for ar in self.get_lista_articulos() if ar.calcular_promedio() == min_promedio]
                if len(lista_restantes_empatados) > 1:
                    
                    lista_seleccionados += lista_restantes_aceptados
                    num_articulos_por_elegir -= len(lista_restantes_aceptados)

                    for pais in self.__lista_paises:
                        for art in lista_restantes_empatados:
                            if art.pertenece_a_pais(pais):
                                art.status = 'ACEPTADO ESPECIAL'
                                lista_seleccionados.append(art)
                                lista_restantes_empatados.remove(art)
                                num_articulos_por_elegir -= 1
                                if num_articulos_por_elegir == 0:
                                    break
                        if num_articulos_por_elegir == 0:
                            break
                    for art in lista_restantes_empatados:
                        art.status = 'RECHAZADO POR FALTA DE CUPO'
                    
                else:
                    for art in primeros_n:
                        art.status = 'ACEPTADO ESPECIAL'
                    lista_seleccionados += primeros_n
                    lista_rechazados_cupo = list(set(self.get_lista_articulos()) - set(primeros_n))
                    for art in lista_rechazados_cupo:
                        art.status = 'RECHAZADO POR FALTA DE CUPO'
                    return lista_seleccionados + lista_rechazados_cupo + self.get_lista_rechazados_articulos()
                    
        return lista_seleccionados + lista_restantes_empatados + self.get_lista_rechazados_articulos()


class ArticuloCortes(ComoSeleccionarArticulos):
    
    # n1 primer numero de corte
    # n2 segundo numero de corte
    __n1 = None
    __n2 = None    
    __lista_paises = []
    
    
    
    # Constructor
    def __init__(self, num_art_aceptar, corte1, corte2):
        super(ArticuloCortes, self).__init__(num_art_aceptar)     
        if not isinstance(corte1, float) or not isinstance(corte2, float):
            raise TypeError
       
        # Calculamos la lista global de paises 
        lista_paises = list(set([autor.pais for autor in Autor.objects.all()]))
        # Y la ordenamos en funcion del numero de participaciones
        lista_paises = sorted(lista_paises,
                                       key=lambda x:calcular_num_participaciones_pais(x))

        self.__n1 = corte1
        self.__n2 = corte2
        self.__lista_paises = lista_paises
            
    def seleccionar_articulos(self):
        #lista_promedios_aceptables = []
        self.set_lista_articulos(sorted(self.get_lista_articulos(),
                                   key=lambda x: x.calcular_promedio(),
                                   reverse=True))            
        lista_promedios_aceptables = [ar for ar in self.get_lista_articulos() if ar.es_aceptable()]
        lista_seleccionados = []
        
            
           
        i = 0
        while i < len(lista_promedios_aceptables) and len(lista_seleccionados) < self.get_num_articulos_aceptar():
            if lista_promedios_aceptables[i].calcular_promedio() >= self.__n1:
                lista_promedios_aceptables[i].status = 'ACEPTADO'
                lista_seleccionados.append(lista_promedios_aceptables[i])
                lista_promedios_aceptables.remove(lista_promedios_aceptables[i])
            else:
                break                
            # segundo corte
        tope = 0
        while tope < len(self.__lista_paises) and len(lista_seleccionados) < self.get_num_articulos_aceptar():
            pais = self.__lista_paises[tope]
            articulo = 0
            while articulo < len(lista_promedios_aceptables) and len(lista_seleccionados) < self.get_num_articulos_aceptar():
            
                aux = lista_promedios_aceptables[articulo]
                print aux
                # ya recorri la lista con promedios aceptables para aceptar con el pais "pais"
                if aux.calcular_promedio() < self.__n2:                        
                    break
                encontrado = False
                k = 0
                for k in aux.autores.all():
                    if k.pais == pais:
                        encontrado = True
                        break
                if encontrado and len(lista_promedios_aceptables)>0:
                    aux.status = 'ACEPTADO ESPECIAL'
                    lista_seleccionados.append(aux)
                    lista_promedios_aceptables.remove(aux)
                else:
                    articulo+=1
            tope += 1
        
        interseccion = list(set(self.get_lista_articulos()) - set(lista_seleccionados))
        if len(lista_seleccionados) == self.get_num_articulos_aceptar():       
            
            for art in interseccion:
                if art.calcular_promedio()>=self.__n2:
                    art.status = 'RECHAZADO POR FALTA DE CUPO'
                else:
                    art.status = 'RECHAZADO POR FALTA DE PROMEDIO'
                    
        else:
            for art in interseccion:
                art.status = 'RECHAZADO POR FALTA DE PROMEDIO'
             
                    
        return lista_seleccionados + interseccion + self.get_lista_rechazados_articulos()
                
            

class ArticuloPorcentaje(ComoSeleccionarArticulos):
    
    __lista_paises = []
    
    def __init__(self, num_art_aceptar):
        super(ArticuloPorcentaje, self).__init__(num_art_aceptar)
        lista_paises = list(set([autor.pais for autor in Autor.objects.all()]))
        # Y la ordenamos en funcion del numero de participaciones
        lista_paises = sorted(lista_paises,
                                       key=lambda x:calcular_num_participaciones_pais(x))
        self.__lista_paises = lista_paises
    
    
    def seleccionar_articulos(self):
        num_articulos = len(self.get_lista_articulos())
        if self.get_num_articulos_aceptar() == 1:
            ochenta_por_ciento = 1
        else:    
            ochenta_por_ciento = self.get_num_articulos_aceptar() * 80 / 100
        veinte_por_ciento = self.get_num_articulos_aceptar() - ochenta_por_ciento
        #self.set_lista_articulos(sorted(self.get_lista_articulos(),
        #                       key=lambda x: x.calcular_promedio()))   
        
        
        matriz_paises = [] # matriz que, por cada pais, guarda los articulos enviados
        for pais in self.__lista_paises:
            lista_articulos_por_pais = []
            for art in self.get_lista_articulos():
                for autor in art.autores.all():
                    if pais == autor.pais:
                        lista_articulos_por_pais.append(art)
                        break
            matriz_paises.append((pais, lista_articulos_por_pais))
           
        # Ahora calculamos el 80 por ciento de los articulos    
        lista_seleccionados = []
        
        for i in matriz_paises:
            j = 0
            while j < len(i[1]): 
                aux = i[1][j]
                if aux in lista_seleccionados:
                    i[1].remove(aux)
                else:   
                    aux.status = 'ACEPTADO'
                    lista_seleccionados.append(aux)
                    self.get_lista_articulos().remove(aux)
                    tam_lista_seleccionados = len(lista_seleccionados)
                    # Chequeo si ya seleccione el 80 por ciento o se me acabaron los articulos
                    if (tam_lista_seleccionados == ochenta_por_ciento or 
                        tam_lista_seleccionados == num_articulos):
                        break
                    
                    i[1].remove(aux)
            tam_lista_seleccionados = len(lista_seleccionados)        
            if (tam_lista_seleccionados == ochenta_por_ciento or 
                tam_lista_seleccionados == num_articulos):
                break
        
        
        if tam_lista_seleccionados < num_articulos:
        # Ahora seleccionamos el 20 por ciento restante 
        # con respecto al mejor promedio
            j = tam_lista_seleccionados
            for i in range(0, veinte_por_ciento):
                if j == num_articulos:
                    break
                articulo_aceptado_especial = self.get_lista_articulos().pop()
                articulo_aceptado_especial.status = 'ACEPTADO ESPECIAL'
                lista_seleccionados.append(articulo_aceptado_especial)
                j += 1
                
        for art in self.get_lista_articulos():
            art.status = 'RECHAZADO POR FALTA DE CUPO'
            
        return lista_seleccionados + self.get_lista_articulos() + self.get_lista_rechazados_articulos()
        
                
class ArticuloTopico(ComoSeleccionarArticulos):
        
    __lista_topicos = []
        
    def __init__(self, num_art_aceptar):
        super(ArticuloTopico, self).__init__(num_art_aceptar)
        self.__lista_topicos = Topico.objects.all()
    
    def seleccionar_articulos(self):
                
        # matriz de tuplas. la tupla en la primera posicion tendra 
        # el topico y en la segunda los articulos asociados
        # a ese topico        
        matriz_topicos = []
        for topi in self.__lista_topicos:
            lista_articulos_por_topico = []
            for art in self.get_lista_articulos():
                for topico in art.topicos.all():
                    if topico.es_igual(topi):
                        lista_articulos_por_topico.append(art)
                        break
            matriz_topicos.append((topi, lista_articulos_por_topico)) 
        lista_seleccionados = []
        
        while len(matriz_topicos) > 0:
            for tupla in matriz_topicos:
                if len(tupla[1]) == 0:
                    matriz_topicos.remove(tupla)
                    break
                else:
                    while True:
                        try:
                            mejor_articulo_topico = tupla[1].pop()
                            if mejor_articulo_topico not in lista_seleccionados:
                                lista_seleccionados.append(mejor_articulo_topico)
                                break
                            continue
                        except: # Entra aqui si ya recorrimos todo los 
                                # articulos del topico
                            matriz_topicos.remove(tupla)
                            break
                                        
                
        lista_rechazados_cupo = []        
        if lista_seleccionados > self.get_num_articulos_aceptar():
            lista_rechazados_cupo = lista_seleccionados[self.get_num_articulos_aceptar():]
            lista_seleccionados = lista_seleccionados[0 : self.get_num_articulos_aceptar()]
            for art in lista_rechazados_cupo:
                art.status = 'RECHAZADOS POR FALTA DE CUPO'
            
        for art in lista_seleccionados:
            art.status = 'ACEPTADO'
            
        return lista_seleccionados + lista_rechazados_cupo + self.get_lista_rechazados_articulos()
            

    

        