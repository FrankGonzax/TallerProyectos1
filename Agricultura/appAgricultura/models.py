from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=40)
    #Huancayo = 1
    #Chupaca = 2
    #Concepcion = 3
    #Jauja = 4
    #Tarma = 5
    #Yauli = 6 
    #Junin = 7

class Cuenta(models.Model):
    cuenta = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

class Temperatura(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    fecha = models.DateField()
    temperatura = models.CharField(max_length=5)

