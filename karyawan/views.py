from django.shortcuts import render, redirect
from .models import KaryawanModels
from .forms import KaryawanForms
from django.contrib.auth.models import Group, User

# Create your views here.

def karyawan(request):
    role = User.objects.get(username = request.user).groups.get()
    karyawan = User.objects.get(id=request.user.id)
    item = KaryawanModels.objects.get(nama = karyawan)
    print(karyawan)
    context = {
        "role":role,
        "karyawan":karyawan,
        "umur":item.umur,
        "img":item.img
    }
    return render(request,"karyawan/karyawan.html",context)

def update(request, update_id):
    karyawan = User.objects.get(id=update_id)
    dataKaryawan = KaryawanModels.objects.get(nama = karyawan)
    data = {
        "username":karyawan.username,
        "umur":dataKaryawan.umur,
        "email":dataKaryawan.email,
    }
    form = KaryawanForms(request.POST or None, initial=data, instance=dataKaryawan)
    context = {
        "heading":"Update",
        "form":form
    }
    if request.method == "POST":
        if form.is_valid():
            karyawan.username = request.POST['nama']
            karyawan.save()
            form.save()
            return redirect("karyawan")
        else:
            print("Tidak Valid")
    return render(request, 'karyawan/update.html',context)