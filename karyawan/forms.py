from django import forms
from .models import KaryawanModels
from django.contrib.auth.models import User

class createKaryawan(forms.ModelForm):
    class Meta:
        model = KaryawanModels
        fields = ['username','email']

class KaryawanForms(forms.ModelForm):
    class Meta:
        model = KaryawanModels
        fields = ['username','umur','email','alamat','telepon']
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'umur': forms.TextInput(attrs={'class': 'form-control'}),
      'email':forms.TextInput(attrs={'class':'form-control'})
    }

    
    def clean_username(self):
        data = self.cleaned_data.get('username')
        if data in User.objects.all():
            raise forms.ValidationError(f"{data} sudah ada")
        return data

class addImage(forms.ModelForm):
    class Meta:
        model = KaryawanModels
        fields = ['img']