from django.db import models
from datetime import date
# Create your models here.



class Trip(models.Model):
    itinerario=models.CharField(max_length=50)
    empresa=models.CharField(max_length=50)
    comentario=models.CharField(max_length=500)
    triper=models.CharField(max_length=50, null=True)
    fecha=models.DateField(default=date.today)
    def __str__(self):
        return f"{self.itinerario} - {self.empresa}"
    


class Aeropuerto(models.Model):
    nombre=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    comentario=models.CharField(max_length=50)
    triper=models.CharField(max_length=50, null=True)
    fecha=models.DateField(default=date.today)
    foto= models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

