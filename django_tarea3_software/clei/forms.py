'''
Created on 15/12/2013

@author: admin
'''

from django import forms 
  
from clei.models import Lugar
from clei.models import Taller
from clei.models import Eventos_Sociales
from clei.models import Apertura
from clei.models import Clausura
from clei.models import MiembroCP
from clei.models import Charlas_Invitadas
from clei.models import CharlistaInvitado
from clei.models import Articulo
from clei.models import Sesiones_Ponencia

  
class RegistrarLugar(forms.ModelForm): 
    ''' 
    Clase para formulario de Lugar 
    '''
    class Meta: 
        model = Lugar
          
      
    def clean(self): 
        return self.cleaned_data
        
class RegistrarTaller(forms.ModelForm): 
    ''' 
    Clase para formulario de taller 
    '''
    class Meta: 
        model = Taller
          
      
    def clean(self): 
        return self.cleaned_data
    
class Registrar_Eventos_Sociales(forms.ModelForm): 
    ''' 
    Clase para formulario de evento social 
    '''
    class Meta: 
        model = Eventos_Sociales
          
      
    def clean(self): 
        return self.cleaned_data

class RegistrarApertura(forms.ModelForm): 
    ''' 
    Clase para formulario de Apertura 
    '''
    class Meta: 
        model = Apertura
          
      
    def clean(self): 
        return self.cleaned_data
    
class RegistrarClausura(forms.ModelForm): 
    ''' 
    Clase para formulario de clausura 
    '''
    class Meta: 
        model = Clausura
          
      
    def clean(self): 
        return self.cleaned_data

class RegistrarMiembroCP(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    class Meta:
        model = MiembroCP
        
    
    def clean(self):
        return self.cleaned_data
    
class RegistrarCharlistaInvitado(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    class Meta:
        model = CharlistaInvitado
        
    
    def clean(self):
        return self.cleaned_data
    
class RegistrarCharlasInvitadas(forms.ModelForm): 
    ''' 
    Clase para formulario de clausura 
    '''
    class Meta: 
        model = Charlas_Invitadas
          
      
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
        
    
    def clean(self):
        
        return self.cleaned_data

class RegistrarSesionesPonencia(forms.ModelForm): 
    ''' 
    Clase para formulario de clausura 
    '''
    class Meta: 
        model = Sesiones_Ponencia
          
      
    def clean(self): 
        return self.cleaned_data