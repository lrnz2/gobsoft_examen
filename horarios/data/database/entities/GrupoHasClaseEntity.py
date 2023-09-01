from django.db import models
from .ClaseEntity import Clase
from .GrupoEntity import Grupo


class GrupoHasClase(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.clase} {self.grupo}"
    
    class Meta:
        unique_together = (("clase", "grupo"),)
