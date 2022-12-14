from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from karyawan.models import KaryawanModels
from .forms import FormKaryawan,FormBaru

# Create your views here.
def admin(request):
    data = User.objects.all()
    context = {
        "data":data,
        "Heading":"Manager"
    }
    print(request.user.groups.filter())
    return render(request,"manager/admin.html",context)

def updateData(request, update_id):
    karyawan = User.objects.get(id=update_id)
    print(User.objects.get(id=update_id))
    data = {
        "email":karyawan.email,
        "username":karyawan.username,
        "password":karyawan.password,
    }
    form = FormBaru(request.POST, initial=data, instance=karyawan)
    context = {
        "heading":"Update",
        "form":form
    }
    if request.method == "POST":
        if form.is_valid():
            karyawan.save()
            return redirect("manager")
    return render(request, "manager/create.html",context)

def createData(request):
    karyawan = User.objects.all()
    form = FormKaryawan(request.POST or None)
    context = {
        "heading":"Create",
        "form":form
    }
    if request.method == "POST":
        if form.is_valid():
            if request.POST['password'] == request.POST['confirmation']:
                karyawan.create(
                    username = request.POST['username'],
                    password = request.POST['password'],
                    email = request.POST['email'],
                )
                #Menambah posisi
                return redirect("manager")
            else:
                return redirect("create")
    return render(request,'manager/create.html',context)

def deleteData(request, delete_id):
    User.objects.filter(id=delete_id).delete()
    return redirect('manager')