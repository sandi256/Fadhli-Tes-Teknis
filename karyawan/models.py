from django.db import models

# Create your models here.


class KaryawanModels(models.Model):
    nama = models.CharField(max_length=50)
    umur = models.IntegerField()
    email = models.EmailField()

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    
