
from django.db import models

# Create your models here.



class Persona(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    fechaInscripcion = models.DateTimeField()
    institucion = models.CharField(max_length=40)
    horaInscripcion = models.TimeField()
    estado = models.CharField(
        max_length=20,
        
    )
    observacion = models.CharField(max_length= 255)
    
class Intituto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreInstituto = models.CharField(max_length=50)
    