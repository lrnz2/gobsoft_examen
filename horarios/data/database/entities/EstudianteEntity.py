from django.db import models

class Estudiante(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    def __str__(self):
        return f"{self.matricula} {self.nombre} {self.apellidos}"
