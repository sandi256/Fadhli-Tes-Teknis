from django.db import models
import os
# Create your models here.

def filepath(request, filename):
    file = filename
    time = models.DateTimeField(auto_now_add=True)
    return os.path.join('img/')

class KaryawanModels(models.Model):
    nama = models.CharField(max_length=50)
    umur = models.IntegerField()
    email = models.EmailField()
    img = models.ImageField(null=True, blank=True, upload_to=filepath)

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)