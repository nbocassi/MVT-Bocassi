from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=120)
    apellido=models.CharField(max_length=120)
    parentezco=models.CharField(null=True, max_length=120)
    ciudad_de_residencia=models.CharField(max_length=120)
    fecha_de_nacimiento=models.DateField()
    pass