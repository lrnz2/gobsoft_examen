from django.db import models
from .DocenteEntity import Docente

class Grupo(models.Model):
    grado = models.CharField(max_length=5, null=False)
    subgrupo = models.CharField(max_length=2, null=False)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.grado} | {self.subgrupo} | {self.docente}"
    class Meta:
        unique_together= (("grado","subgrupo","docente"))
