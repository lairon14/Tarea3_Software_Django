'''
Created on 14/12/2013

@author: HP
'''
from django import forms
from django.contrib import admin
from django.forms.widgets import HiddenInput
from django.template.loader import render_to_string 

from demo.apps.clei.models import MiembroCP, Articulo, Evaluacion, Topico, Autor


class RegistrarMiembroCP(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    
    def __init__(self, *args, **kwargs):
        super(RegistrarMiembroCP, self).__init__(*args, **kwargs)
        # Verifico si ya el presidente esta
        # agregado a la base de datos
        for cp in MiembroCP.objects.all():
            if cp.es_presidente == True:
                self.fields["es_presidente"].widget = HiddenInput()
    class Meta:
        model = MiembroCP
                
        
    
    def clean(self):
        return self.cleaned_data


class RegistrarTopico(forms.ModelForm):
    '''
    Clase para formulario de registro de topico
    '''
    class Meta:
        model = Topico
              
  
    def clean_nombre(self):
        nombre_topico = self.cleaned_data['nombre']
        # No debe haber 2 topicos con un mismo nombre
        try:
            topico = Topico.objects.get(nombre=nombre_topico)
        except:
            return nombre_topico        
        raise forms.ValidationError("Nombre de topico ya existe")

    def clean(self):
        return self.cleaned_data

class RegistrarAutorForm(forms.ModelForm):
    '''
    Clase para formulario de registro de topico
    '''
    class Meta:
        model = Autor
                
    
    def clean(self):
        return self.cleaned_data


    
class RegistrarArticuloForm(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    def __init__(self, *args, **kwargs):
        super(RegistrarArticuloForm, self).__init__(*args, **kwargs)
        self.fields['p2'].required = False
        self.fields['p3'].required = False
        self.fields['p4'].required = False
        self.fields['p5'].required = False

    class Meta:
        model = Articulo
        exclude = ('status',)

    def clean_titulo(self):
        titulo_articulo = self.cleaned_data['titulo']
        # No debe haber 2 articulos con un mismo titulo
        for art in Articulo.objects.all():
            if art.titulo == titulo_articulo:
                self._errors['title'] = ['Invalid date given.']
                raise forms.ValidationError(u'El titulo del articulo ya existe')
        return titulo_articulo

    def clean(self):
        return self.cleaned_data

        
    
class RegistrarEvaluacionForm(forms.ModelForm):
    '''
    Clase para formulario de evaluaciones
    '''
    class Meta:
        model = Evaluacion
        
    def clean(self):
        
        return self.cleaned_data
       
    
        
        
