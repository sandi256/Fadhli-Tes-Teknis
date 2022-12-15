from django import forms
from .models import EditUser
from django.contrib.auth.models import User

class FormKaryawan(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    confirmation = forms.CharField(max_length=20,widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data.get("username")
        if data in User.objects.all():
            raise forms.ValidationError(f"{data} sudah ada")
        return data