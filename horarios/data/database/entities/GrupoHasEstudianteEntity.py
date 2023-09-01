from django.db import models
from .EstudianteEntity import Estudiante
from .GrupoEntity import Grupo

class GrupoHasEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    def __str__(self):
        return f"Estudiante: {self.estudiante} \nGrupo: {self.grupo}"
    
    class Meta:
        unique_together =(("estudiante", "grupo"),)
