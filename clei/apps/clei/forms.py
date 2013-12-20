'''
Created on 14/12/2013

@author: HP
'''
from django import forms
from django.forms.widgets import HiddenInput

from demo.apps.clei.models import MiembroCP, Articulo, Evaluacion, Topico, Autor


class RegistrarMiembroCPForm(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    
    def __init__(self, *args, **kwargs):
        super(RegistrarMiembroCPForm, self).__init__(*args, **kwargs)
        # Verifico si ya el presidente esta
        # agregado a la base de datos
        for cp in MiembroCP.objects.all():
            if cp.es_presidente == True:
                self.fields["es_presidente"].widget = HiddenInput()
    class Meta:
        model = MiembroCP
                
        
    
    def clean(self):
        return self.cleaned_data


class RegistrarTopicoForm(forms.ModelForm):
    '''
    Clase para formulario de registro de topico
    '''
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Topico
              
    # Validacion del campo nombre
    def clean_nombre(self):
        nombre_topico = self.cleaned_data['nombre']
        # No debe haber 2 topicos con un mismo nombre
        for topico in Topico.objects.all():
            if topico.nombre == nombre_topico:
                raise forms.ValidationError(u'Nombre de topico ya existe')
            
        return nombre_topico

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

    # Validacion del campo titulo
    def clean_titulo(self):
        titulo_articulo = self.cleaned_data['titulo']
        # No debe haber 2 articulos con un mismo titulo
        for art in Articulo.objects.all():
            if art.titulo == titulo_articulo:
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
      
    # Validacion del formulario  
    def clean(self):
        # los topicos del miembro del cp y los del articulo deben coincidir
        cp = self.cleaned_data.get('miembro_cp')
        articulo = self.cleaned_data.get('articulo')
        nota = self.cleaned_data.get('nota')
        evaluacion = Evaluacion(miembro_cp = cp,
                          articulo = articulo,
                          nota = nota)
        if not evaluacion.coinciden_topicos():
            raise forms.ValidationError(u'Los topicos no coinciden')
        # Ahora verificamos que la evaluacion no este repetida
        if evaluacion.existe_evaluacion():
            raise forms.ValidationError(u'Ya la evaluacion existe') 
        
        return self.cleaned_data
       
    
        
        
