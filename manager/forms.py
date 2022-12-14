from django import forms
from .models import EditUser

class FormKaryawan(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    confirmation = forms.CharField(max_length=20,widget=forms.PasswordInput)

class FormBaru(forms.ModelForm):
    class Meta:
        model = EditUser
        fields = '__all__'