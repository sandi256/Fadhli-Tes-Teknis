from django.db import models

# Create your models here.
class EditUser(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirmation = models.CharField(max_length=20)