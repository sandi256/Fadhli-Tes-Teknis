from django.db import models
import os
from slugify import slugify
# Create your models here.

class KaryawanModels(models.Model):
    username = models.CharField(max_length=50)
    umur = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    img = models.ImageField(null=True, blank=True, upload_to='static/img/')

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ("Admin","Can change karyawan"),
            ("Karyawan","Only Profile")
        )

    def __str__(self):
        return "{}".format(self.username)
    