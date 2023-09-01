from django.db import models

class Docente(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=50, null=False)
    def __str__(self):
        return f"{self.matricula} {self.nombre} {self.apellidos}"
