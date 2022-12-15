from django import forms
from .models import KaryawanModels

class KaryawanForms(forms.ModelForm):
    class Meta:
        model = KaryawanModels
        fields = ['username','umur','email']

class addImage(forms.ModelForm):
    class Meta:
        model = KaryawanModels
        fields = ['img']