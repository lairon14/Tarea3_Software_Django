from django import forms

from clei.apps.inscripciones.models import Participante, Inscripcion


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante 
        exlude = ['fecha']
        
class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
