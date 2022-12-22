from django import forms
from app.models import Persona

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'