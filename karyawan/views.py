from django.shortcuts import render
from .models import KaryawanModels
from django.contrib.auth.models import Group, User

# Create your views here.

def karyawan(request):
    role = User.objects.get(username = request.user).groups.get()
    context = {
        "role":role,
    }
    print(request.user)
    print(request.user.groups.get())
    return render(request,"karyawan/karyawan.html",context)