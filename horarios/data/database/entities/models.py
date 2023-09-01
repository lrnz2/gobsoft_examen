from django.db import models

from .DocenteEntity import DocenteEntity
from .EstudianteEntity import EstudianteEntity
from .ClaseEntity import ClaseEntity
from .GrupoEntity import GrupoEntity
from .MateriaEntity import MateriaEntity
from .GrupoHasClaseEntity import GrupoHasClaseEntity
from .GrupoHasEstudianteEntity import GrupoHasEstudianteEntity


"""
class Estudiante(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    def __str__(self):
        return f"{self.matricula} {self.nombre} {self.apellidos}"

class Docente(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=50, null=False)
    def __str__(self):
        return f"{self.matricula} {self.nombre} {self.apellidos}"

class Materia(models.Model):
    clave = models.CharField(max_length=15, primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, unique=True, null=False)
    creditos = models.CharField(max_length=5, null=False)
    def __str__(self):
        return f"{self.nombre}"

class Clase(models.Model):
    materia = models.ForeignKey( Materia , on_delete= models.DO_NOTHING)
    docente = models.ForeignKey( Docente , on_delete= models.DO_NOTHING)
    hora = models.CharField(max_length=15)
    dia = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.hora} {self.dia} {self.materia} {self.docente}"
    class Meta:
        unique_together =(("materia","hora","dia",))

class Grupo(models.Model):
    grado = models.CharField(max_length=5, null=False)
    subgrupo = models.CharField(max_length=2, null=False)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.grado} | {self.subgrupo} | {self.docente}"
    class Meta:
        unique_together= (("grado","subgrupo","docente"))

class ClaseHasGrupo(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.clase} {self.grupo}"
    
    class Meta:
        unique_together = (("clase", "grupo"),)

class EstudianteHasGrupo(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.estudainte} {self.grupo}"
    
    class Meta:
        unique_together =(("estudiante", "grupo"),)
"""