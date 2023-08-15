from django.db import models
from django.utils import timezone
# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField("Hora de inicio", default=timezone.now)
    hora_fin = models.TimeField("Hora de fin", default=timezone.now)
    def __str__(self):
        return self.nombre

class Materias_Por_Alumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    def __str__(self):
        return ("(Alumno) %s, (Materia) %s") % (self.alumno, self.materia)

class Materias_Por_Maestro(models.Model):
    maestro = models.ForeignKey(Maestro, on_delete=models.DO_NOTHING)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    def __str__(self):
        return ("%s, Impartida por: %s") % (self.materia, self.maestro)

class Alumnos_Por_Maestro(models.Model):
    maestro = models.ForeignKey(Maestro, on_delete=models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    def __str__(self):
        return ("Maestro: %s, Alumno: %s") % (self.maestro, self.alumno)

