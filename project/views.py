from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

def loginView(request):
    form = LoginForm()
    context = {
        "heading":"Login",
        "form":form
    }
    if request.method == "POST":
        user = request.POST["username"]
        sandi = request.POST["password"]
        akun = authenticate(username=user, password=sandi)
        if akun is not None:
            login(request, akun)
            print('Success')
            user_group = request.user.groups.all()
            grup = user_group[0]
            if grup == Group.objects.get(name="Admin") :
                return redirect('/manager/')
            else:
                return redirect('/karyawan/')
        else:
            print("Tidak ada akun")
    return render(request,'login.html',context)
