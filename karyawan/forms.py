from django import forms
from .models import KaryawanModels

class KaryawanForms(forms.ModelForm):
    class Meta:
        model = KaryawanModels
        fields = '__all__'