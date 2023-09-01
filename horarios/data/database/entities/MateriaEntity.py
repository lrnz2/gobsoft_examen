from django.db import models

class Materia(models.Model):
    clave = models.CharField(max_length=15, primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, unique=True, null=False)
    creditos = models.CharField(max_length=5, null=False)
    def __str__(self):
        return f"{self.nombre}"
