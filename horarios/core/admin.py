from django.contrib import admin
#from ..data.database.entities.models import *
from horarios.data.database.entities.ClaseEntity import *
from horarios.data.database.entities.DocenteEntity import *
from horarios.data.database.entities.EstudianteEntity import *
from horarios.data.database.entities.GrupoEntity import *
from horarios.data.database.entities.MateriaEntity import *
from horarios.data.database.entities.GrupoHasClaseEntity import *
from horarios.data.database.entities.GrupoHasEstudianteEntity import *

admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Clase)
admin.site.register(Grupo)
admin.site.register(GrupoHasClase)
admin.site.register(GrupoHasEstudiante)