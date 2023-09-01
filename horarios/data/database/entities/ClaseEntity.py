from django.db import models
from .MateriaEntity import Materia
from .DocenteEntity import Docente

class Clase(models.Model):
    materia = models.ForeignKey( Materia , on_delete= models.CASCADE)
    docente = models.ForeignKey( Docente , on_delete= models.CASCADE)
    hora = models.CharField(max_length=15)
    dia = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.hora} {self.dia} {self.materia} {self.docente}"
    class Meta:
        unique_together =(("materia","hora","dia",))
