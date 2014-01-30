
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


# Esta vaina se debe de cambiar, el nombre NO PDE SER FORM
# OJOOO
#
# CAMBIAAAAAR NO TE OLVIDEEES
#
class NForm(forms.Form):
    
    n = forms.IntegerField(validators=[MinValueValidator(1)])
    
    def clean(self):
        return self.cleaned_data
    
class CortesForm(NForm):
    corte1 = forms.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    corte2 = forms.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
class MinPForm(NForm):
    min_p = forms.IntegerField(validators=[MinValueValidator(1)])
