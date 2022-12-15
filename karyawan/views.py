from django.shortcuts import render, redirect
from .models import KaryawanModels
from .forms import KaryawanForms, addImage
from django.contrib.auth.models import Group, User

# Create your views here.

def karyawan(request):
    role = User.objects.get(username = request.user).groups.get()
    username = User.objects.get(id=request.user.id)
    karyawan = KaryawanModels.objects.get(username = username)
    print(karyawan.telepon)
    context = {
        "heading":"Profile Karyawan",
        "role":role,
        "karyawan":username,
        "umur":karyawan.umur,
        "alamat":karyawan.alamat,
        "telepon":karyawan.telepon,
        "img":karyawan.img,
    }
    return render(request,"karyawan/karyawan.html",context)

def update(request, update_id):
    karyawan = User.objects.get(id=update_id)
    dataKaryawan = KaryawanModels.objects.get(username = karyawan)
    data = {
        "username":karyawan.username,
        "umur":dataKaryawan.umur,
        "email":dataKaryawan.email,
    }
    form = KaryawanForms(request.POST or None, initial=data, instance=dataKaryawan)
    image = addImage(request.POST or None ,request.FILES, initial=data, instance=dataKaryawan)
    context = {
        "heading":"Update",
        "form":form,
        "img":image
    }
    if request.method == "POST":
        if form.is_valid():
            karyawan.username = request.POST['username']
            karyawan.save()
            image.save()
            form.save()
            return redirect("karyawan")
        else:
            print("Tidak Valid")
    return render(request, 'karyawan/update.html',context)