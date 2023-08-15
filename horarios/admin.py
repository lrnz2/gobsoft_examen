from django.contrib import admin
from .models import Alumno, Materia, Maestro, Materias_Por_Maestro, Materias_Por_Alumno, Alumnos_Por_Maestro

admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Maestro)
admin.site.register(Materias_Por_Maestro)
admin.site.register(Materias_Por_Alumno)
admin.site.register(Alumnos_Por_Maestro)