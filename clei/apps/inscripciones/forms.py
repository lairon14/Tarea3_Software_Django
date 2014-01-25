from django import forms

from clei.apps.inscripciones.models import Participante, Inscripcion


class ParticipanteForm(forms.ModelForm):
    url = forms.URLField(required=False)
    class Meta:
        model = Participante 
        exclude = ['fecha']
        
class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        exclude = ['costo', 'descuento', 'fecha_inscripcion','eventos', 'pago_realizado']